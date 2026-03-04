"""from typing import List
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session

from .config import Settings
from .database import Base, engine, get_db
from . import models, schemas

app = FastAPI(title="Books Service", version="1.0.0")

# Create tables at startup (simple approach for this assignment)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}

# --- CRUD for Books ---

@app.post(
    "/api/v1/books",
    response_model=schemas.BookOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Books"],
)
def create_book(payload: schemas.BookCreate, db: Session = Depends(get_db)):
    book = models.Book(title=payload.title, author=payload.author, description=payload.description)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@app.get("/api/v1/books", response_model=List[schemas.BookOut], tags=["Books"])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.get("/api/v1/books/{book_id}", response_model=schemas.BookOut, tags=["Books"])
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
    return book

@app.put("/api/v1/books/{book_id}", response_model=schemas.BookOut, tags=["Books"])
def update_book(book_id: int, payload: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")

    if payload.title is not None:
        book.title = payload.title
    if payload.author is not None:
        book.author = payload.author
    if payload.description is not None:
        book.description = payload.description

    db.add(book)
    db.commit()
    db.refresh(book)
    return book

@app.delete("/api/v1/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Books"])
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail=f"Book {book_id} not found")
    db.delete(book)
    db.commit()
    return None

# Allow `python -m app.main` to run locally without uvicorn CLI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=Settings.APP_HOST, port=Settings.APP_PORT, reload=Settings.DEBUG)"""






from fastapi import FastAPI, HTTPException
from typing import List
from app.models import Book
import os

app = FastAPI()

PORT = int(os.getenv("PORT", 8000))

books: List[Book] = []

@app.get("/")
def root():
    return {"message": "Book CRUD Microservice is running"}

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return {"message": "Book created successfully", "book": book}

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return {"message": "Book updated", "book": updated_book}
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted = books.pop(index)
            return {"message": "Book deleted", "book": deleted}
    raise HTTPException(status_code=404, detail="Book not found")
