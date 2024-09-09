from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import client as models
from models import SessionLocal
from models.client import Client

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/clients")
def get_clients(db: Session = Depends(get_db)):
    return db.query(models.Client).all()

@router.post("/clients")
def add_client(client: Client, db: Session = Depends(get_db)):
    db_client = models.Client(
        name=client.name,
        email=client.email,
        phone_number=client.phone_number
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/clients/{client_id}")
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/clients/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db.delete(client)
    db.commit()
    return {"detail": "Client deleted"}
