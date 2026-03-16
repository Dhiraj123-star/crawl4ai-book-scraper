from pydantic import BaseModel
from typing import List

class Book(BaseModel):
    title: str
    price: str

class BookList(BaseModel):
    books: List[Book]