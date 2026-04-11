from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

books_db = []

@app.post("/books/", response_model=Book)
def create_book(book: Book):
    books_db.append(book)
    return book

@app.get("/books/", response_model=List[Book])
def get_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            books_db[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[idx]
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")