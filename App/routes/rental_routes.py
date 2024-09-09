from fastapi import APIRouter
from models.rental import Rental

router = APIRouter()

rentals = []

@router.get("/rentals")
def get_rentals():
    return rentals

@router.post("/rentals")
def add_rental(rental: Rental):
    rentals.append(rental)
    return rental