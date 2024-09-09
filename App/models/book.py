from pydantic import BaseModel
from models.author import Author

class Book(BaseModel):
    id: int
    title: str
    genre: str
    author: Author
    publisher_id: int