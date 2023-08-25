from loguru import logger
from sqlalchemy import and_
from sqlalchemy.sql import func
from sqlalchemy.exc import IntegrityError

from models import Joke


class JokeRepository:
    def __init__(self, session):
        self.session = session

    def get_random_joke(self, limit=1):
        return self.session.query(Joke).filter_by(approved=True).order_by(
            func.rand()).limit(limit)

    def get_by_category(self, category, offset: int, limit: int):
        return self.session.query(Joke).filter_by(
            category=category, approved=True).offset(offset).limit(limit)

    def get(self, offset: int, limit: int, kwargs):
        return self.session.query(Joke).filter_by(**kwargs).offset(offset).limit(limit)

    def search(self, phrase):
        return self.session.query(Joke).filter(
            and_(Joke.body.contains(phrase), Joke.approved == True)).all()

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
        return self.session.query(Joke).filter_by(id=_id).update(
            {"approved": True})
