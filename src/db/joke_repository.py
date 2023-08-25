from loguru import logger
from sqlalchemy import and_
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError
from models import Joke


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class JokeRepository:
    __metaclass__ = Singleton

    def __init__(self, session):
        self.session = session

    def get_random_joke(self, limit: int):
        return self.session.query(Joke).filter_by(approved=True).order_by(
            func.rand()).limit(limit)

    def get_by_category(self, category, offset: int, limit: int):
        return self.session.query(Joke).filter_by(
            category=category, approved=True).offset(offset).limit(limit)

    def get(self, offset: int, limit: int, kwargs):
        return self.session.query(Joke).filter_by(**kwargs).offset(
            offset).limit(limit)

    def search(self, phrase: str, offset: int, limit: int):
        return self.session.query(Joke).filter(
            and_(Joke.body.contains(phrase), Joke.approved == True)).offset(
            offset).limit(limit)

    def get_all_categories(self):
        return self.session.query(Joke.category).filter(
            Joke.approved == True).distinct().all()

    def add(self, joke):
        try:
            self.session.add(joke)
            self.session.commit()
            return
        except IntegrityError:
            logger.warning(f'Duplicate joke: {joke.body}')
        except Exception as e:
            logger.error(e)
        self.session.rollback()

    def delete(self, joke):
        try:
            self.session.delete(joke)
            self.session.commit()
            return
        except Exception as e:
            logger.error(e)
        self.session.rollback()

    def approve(self, _id):
        try:
            resp = self.session.query(Joke).filter_by(id=_id).update(
                {"approved": True})
            self.session.commit()
            return resp
        except Exception as e:
            logger.error(e)
        self.session.rollback()
        return 0
