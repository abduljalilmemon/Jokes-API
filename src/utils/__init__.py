from db import session
from db.joke_repository import JokeRepository
from models import Joke


def add_joke(joke: str, category: str):
    new_joke = Joke(body=joke, category=category)
    joke_repository = JokeRepository(session)
    joke_repository.add(new_joke)
    return True
