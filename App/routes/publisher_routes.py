from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import publisher as models
from models import SessionLocal
from models.publisher import Publisher

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/publishers")
def get_publishers(db: Session = Depends(get_db)):
    return db.query(models.Publisher).all()

@router.post("/publishers")
def add_publisher(publisher: Publisher, db: Session = Depends(get_db)):
    db_publisher = models.Publisher(
        name=publisher.name,
        country=publisher.country
    )
    db.add(db_publisher)
    db.commit()
    db.refresh(db_publisher)
    return db_publisher

@router.get("/publishers/{publisher_id}")
def get_publisher(publisher_id: int, db: Session = Depends(get_db)):
    publisher = db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()
    if publisher is None:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher

@router.delete("/publishers/{publisher_id}")
def delete_publisher(publisher_id: int, db: Session = Depends(get_db)):
    publisher = db.query(models.Publisher).filter(models.Publisher.id == publisher_id).first()
    if publisher is None:
        raise HTTPException(status_code=404, detail="Publisher not found")
    db.delete(publisher)
    db.commit()
    return {"detail": "Publisher deleted"}
