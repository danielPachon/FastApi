from fastapi import APIRouter
from models.publisher import Publisher

router = APIRouter()

publishers = []

@router.get("/publishers")
def get_publishers():
    return publishers

@router.post("/publishers")
def add_publisher(publisher: Publisher):
    publishers.append(publisher)
    return publisher