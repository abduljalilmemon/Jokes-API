from db import session
from db.joke_repository import JokeRepository
from models import Joke
from config import USERS
from auth.auth_handler import generate_token


def auth_user(username, password):
    user = USERS.get(username)
    if user and (user.get("password") == password):
        return True, generate_token(username)
    return False, "username or password is invalid"


def add_joke(joke: str, category: str):
    new_joke = Joke(body=joke, category=category)
    joke_repository = JokeRepository(session)
    joke_repository.add(new_joke)
    return True


def get_random_joke(limit: int = 1):
    joke_repository = JokeRepository(session)
    jokes = joke_repository.get_random_joke(limit)
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]


def search_joke(phrase: str, offset: int = 0, limit: int = 1):
    joke_repository = JokeRepository(session)
    jokes = joke_repository.search(phrase=phrase, limit=limit, offset=offset)
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]


def get_joke_from_category(category: str, offset: int = 0, limit: int = 1):
    joke_repository = JokeRepository(session)
    jokes = joke_repository.get_by_category(category=category.lower(),
                                            offset=offset, limit=limit)
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]


def get_unapproved_jokes(offset: int, limit: int):
    joke_repository = JokeRepository(session)
    kwargs = {"approved": False}
    jokes = joke_repository.get(offset=offset, limit=limit, kwargs=kwargs)
    return [{"joke": joke.body, "category": joke.category, "id": joke.id} for
            joke in jokes]


def approve_joke(_id: str):
    joke_repository = JokeRepository(session)
    return joke_repository.approve(_id=_id)
