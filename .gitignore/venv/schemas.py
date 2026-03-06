from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    category: str
    rating: int
    notes: str