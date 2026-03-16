from fastapi import FastAPI, HTTPException, Query
import json
from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Book Scraper API")

DATA_FILE = Path("data/books.json")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_books():
    if not DATA_FILE.exists():
        raise HTTPException(
            status_code=404,
            detail="Books data not found. Run the scraper first."
        )
    with open(DATA_FILE) as f:
        return json.load(f)

@app.get("/")
def root():
    return {"message":"Book Scrapper API is running"}
# ------------------
# GET all books
# ------------------

@app.get("/books")
def get_books(title: str | None =Query(None)):
    data = load_books()
    books =data.get("books",[])

    if title:
        for book in books:
            if title.lower() in book["title"].lower():
                return book
        raise HTTPException(status_code=404,detail="Book not found")
    return books

# -----------------------
# AI Question Answering
# ------------------------
@app.get("/ask")
def ask_books(question:str):
    data = load_books()
    prompt = f"""
You are a helpful assistant answering questions about a dataset of books.
Book dataset:

{json.dumps(data)}

Answer the user question strictly using the dataset.

User question:
{question}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"You answer questions about books dataset."},
            {"role":"user","content": prompt}
        ],
        temperature=0
    )
    answer= response.choices[0].message.content

    return {
        "question":question,
        "answer":answer
    }
