# app/crud.py

from typing import List, Optional
from .models import Book

# This list simulates a database for demonstration purposes
books_db: List[Book] = []

def create_book(book: Book) -> Book:
    books_db.append(book)
    return book

def get_books() -> List[Book]:
    return books_db

def get_book(book_id: int) -> Optional[Book]:
    for book in books_db:
        if book.id == book_id:
            return book
    return None

def update_book(book_id: int, updated_book: Book) -> Optional[Book]:
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            books_db[idx] = updated_book
            return updated_book
    return None

def delete_book(book_id: int) -> bool:
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[idx]
            return True
    return False