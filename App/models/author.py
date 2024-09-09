from sqlalchemy import Column, Integer, String
from . import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    nationality = Column(String(100))
    birth_date = Column(String(10))
