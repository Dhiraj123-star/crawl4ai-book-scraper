import json
from openai import OpenAI
import re
import os
from dotenv import load_dotenv
from rag.vector_store import BookVectorStore

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

store = BookVectorStore()
store.load_books()
store.create_embeddings()

def extract_price_condition(question:str):
    """
    Detect price conditions like:
    - less than 50
    - greater than 30
    - equal to 20
    - less than or equal to 40
    - greater than or equal to 25
    """
    question = question.lower()

    patterns = [
        (r"(less than or equal to|<=)\s*(\d+)", "<="),
        (r"(greater than or equal to|>=)\s*(\d+)", ">="),
        (r"(less than|lower than|under)\s*(\d+)", "<"),
        (r"(greater than|higher than|above)\s*(\d+)", ">"),
        (r"(equal to|exactly)\s*(\d+)", "=="),
    ]
    for pattern,operator in patterns:
        match = re.search(pattern,question)
        if match:
            return operator,float(match.group(2))

def filter_books_by_price(operator:str,value:str):
    results=[]
    for book in store.books:
        price = float(book["price"].replace("£", ""))

        if (
            (operator == "<" and price < value) or
            (operator == ">" and price > value) or
            (operator == "==" and price == value) or
            (operator == "<=" and price <= value) or
            (operator == ">=" and price >= value)
        ):
            results.append(book)
    return results

def rag_answer(question:str):
    operator,value = extract_price_condition(question)
    if operator:
        retrieved_books = filter_books_by_price(operator,value)
    else:
        retrieved_books = store.search(question,k=10)
    context = json.dumps(retrieved_books,indent=2)
    prompt = f"""

You are answering questions about books.
Relevant books:

{context}

Answer the question using only the provided books.

Question:
{question}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"Answer questions using the retrieved books."},
            {"role":"user","content":prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content