from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import book as models
from models import SessionLocal
from models.book import Book

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router.post("/books")
def add_book(book: Book, db: Session = Depends(get_db)):
    db_book = models.Book(
        title=book.title, 
        genre=book.genre, 
        author_id=book.author_id, 
        publisher_id=book.publisher_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/books/{book_id}")
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted"}
