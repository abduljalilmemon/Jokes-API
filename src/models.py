from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Joke(Base):
    __tablename__ = 'joke'

    id = Column(Integer, primary_key=True)
    body = Column(String)
    category = Column(String)
    approved = Column(Boolean, default=False)
