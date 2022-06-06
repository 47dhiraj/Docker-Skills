from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Book(Base):
    __tablename__ = "book"                                          # FastAPI ma yesari table lai name dine garincha
    id = Column(Integer, primary_key=True, index=True)              # FastAPI ma yesari id field pani lekhne garincha
    title = Column(String)                                          # title String field  
    rating = Column(Integer)                                    
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    author_id = Column(Integer, ForeignKey("author.id"))            # ForeignKey vannale One to Many relationship

    author = relationship("Author")


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
