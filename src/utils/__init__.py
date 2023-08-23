from db import session
from db.joke_repository import JokeRepository
from models import Joke


def add_joke(joke: str, category: str):
    new_joke = Joke(body=joke, category=category)
    joke_repository = JokeRepository(session)
    joke_repository.add(new_joke)
    return True


def get_random_joke():
    joke_repository = JokeRepository(session)
    jokes = joke_repository.get_random_joke()
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]


def search_joke(phrase: str):
    joke_repository = JokeRepository(session)
    jokes = joke_repository.search(phrase=phrase)
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]


def get_joke_from_category(category: str, offset: int, limit: int):
    joke_repository = JokeRepository(session)
    jokes = joke_repository.get_by_category(category=category.lower(),
                                            offset=offset, limit=limit)
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]
