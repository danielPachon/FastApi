from pydantic import BaseModel

class Author(BaseModel):
    id: int
    name: str
    nationality: str
    birth_date: str
