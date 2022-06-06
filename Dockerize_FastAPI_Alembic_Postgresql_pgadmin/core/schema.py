from pydantic import BaseModel

# API batw data transfer huda kheri, kun kun field ko data transfer huncha and kasto data type ko data transfer huncha vanne kura schema.py file ma class banayera lekhincha
class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        orm_mode = True


class Author(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True


