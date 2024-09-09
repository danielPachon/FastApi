from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import rental as models
from models import SessionLocal
from models.rental import Rental

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/rentals")
def get_rentals(db: Session = Depends(get_db)):
    return db.query(models.Rental).all()

@router.post("/rentals")
def add_rental(rental: Rental, db: Session = Depends(get_db)):
    db_rental = models.Rental(
        book_id=rental.book_id,
        client_id=rental.client_id,
        rental_date=rental.rental_date,
        return_date=rental.return_date
    )
    db.add(db_rental)
    db.commit()
    db.refresh(db_rental)
    return db_rental

@router.get("/rentals/{rental_id}")
def get_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = db.query(models.Rental).filter(models.Rental.id == rental_id).first()
    if rental is None:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental

@router.delete("/rentals/{rental_id}")
def delete_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = db.query(models.Rental).filter(models.Rental.id == rental_id).first()
    if rental is None:
        raise HTTPException(status_code=404, detail="Rental not found")
    db.delete(rental)
    db.commit()
    return {"detail": "Rental deleted"}
