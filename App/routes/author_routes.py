from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import author as models
from models import author
from models import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/authors")
def get_authors(db: Session = Depends(get_db)):
    return db.query(models.Author).all()

@router.post("/authors")
def add_author(author: author.Author, db: Session = Depends(get_db)):
    db_author = models.Author(name=author.name, nationality=author.nationality, birth_date=author.birth_date)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author
