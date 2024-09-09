from pydantic import BaseModel
from models.book import Book
from models.client import Client

class Rental(BaseModel):
    id: int
    book: Book
    client: Client
    rental_date: str
    return_date: str