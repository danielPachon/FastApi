from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Rental(Base):
    __tablename__ = "rentals"

    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    client_id = Column(Integer, ForeignKey('clients.id'))
    rental_date = Column(String(10))
    return_date = Column(String(10))

    book = relationship("Book")
    client = relationship("Client")
