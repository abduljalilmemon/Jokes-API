from loguru import logger
from sqlalchemy.exc import IntegrityError

from models import Joke


class JokeRepository:
    def __init__(self, session):
        self.session = session

    def get_by_category(self, category):
        return self.session.query(Joke).filter_by(category=category).all()

    def add(self, joke):
        try:
            self.session.add(joke)
            self.session.commit()
            return
        except IntegrityError as i:
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
