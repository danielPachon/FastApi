from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    country = Column(String(100))

    books = relationship("Book", back_populates="publisher")
