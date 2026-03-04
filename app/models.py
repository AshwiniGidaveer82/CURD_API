"""from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=True)"""




from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
