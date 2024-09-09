from fastapi import APIRouter
from models.author import Author

router = APIRouter()

authors = []

@router.get("/authors")
def get_authors():
    return authors

@router.post("/authors")
def add_author(author: Author):
    authors.append(author)
    return author