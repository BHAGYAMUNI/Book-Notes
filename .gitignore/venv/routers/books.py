from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/books")
def create_book(book: schemas.Book, db: Session = Depends(get_db)):
    new_book = models.Book(
        title=book.title,
        author=book.author,
        category=book.category,
        rating=book.rating,
        notes=book.notes
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books


@router.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    return book


@router.put("/books/{book_id}")
def update_book(book_id: int, updated_book: schemas.Book, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book:
        book.title = updated_book.title
        book.author = updated_book.author
        book.category = updated_book.category
        book.rating = updated_book.rating
        book.notes = updated_book.notes

        db.commit()
        db.refresh(book)

        return {"message": "Book updated", "book": book}

    return {"error": "Book not found"}


@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if book:
        db.delete(book)
        db.commit()
        return {"message": "Book deleted"}

    return {"error": "Book not found"}