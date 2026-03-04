"""from typing import Optional
from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None

class BookOut(BookBase):
    id: int
    # Pydantic v2-style config to read ORM objects
    model_config = ConfigDict(from_attributes=True)"""