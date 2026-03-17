import json
import numpy as np
from pathlib import Path
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DATA_FILE = Path("data/books.json")

class BookVectorStore:
    def __init__(self):
        self.books =[]
        self.embeddings=None
    
    def load_books(self):
        with open(DATA_FILE) as f:
            data = json.load(f)
        self.books=data["books"]
    
    def create_embeddings(self):
        texts=[
            f"{book['title']} price {book['price']}"
            for book in self.books
        ]
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        vectors = [item.embedding for item in response.data]

        self.embeddings = np.array(vectors)

    def search(self,query,k=5):
        query_embeddings = client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        ).data[0].embedding

        query_vector = np.array(query_embeddings)
        similarities = np.dot(self.embeddings,query_vector)

        top_k_indices = np.argsort(similarities)[-k:][::-1]
        return [self.books[i] for i in top_k_indices]