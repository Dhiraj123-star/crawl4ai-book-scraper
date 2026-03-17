import json
from openai import OpenAI
import os
from dotenv import load_dotenv
from rag.vector_store import BookVectorStore

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

store = BookVectorStore()
store.load_books()
store.create_embeddings()

def rag_answer(question:str):
    retrieved_books = store.search(question,k=5)

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