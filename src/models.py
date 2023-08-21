from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Joke(Base):
    __tablename__ = 'joke'

    id = Column(Integer, primary_key=True)
    body = Column(String)
    category = Column(String)
