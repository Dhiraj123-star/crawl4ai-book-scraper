from fastapi import FastAPI, HTTPException, Query
import json
from pathlib import Path

app = FastAPI(title="Book Scraper API")

DATA_FILE = Path("data/books.json")

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
