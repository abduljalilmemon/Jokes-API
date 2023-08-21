from models import Joke


class JokeRepository:
    def __init__(self, session):
        self.session = session

    def get_by_category(self, category):
        return self.session.query(Joke).filter_by(category=category).all()

    def add(self, joke):
        self.session.add(joke)
        self.session.commit()

    def delete(self, joke):
        self.session.delete(joke)
        self.session.commit()
