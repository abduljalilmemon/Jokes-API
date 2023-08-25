from db import session
from db.joke_repository import JokeRepository
from models import Joke
from config import USERS, QUOTA
from auth.auth_handler import generate_token
from schemas import UserAuth
from uuid import uuid4
from auth.auth_handler import get_hashed_password
from fastapi.responses import JSONResponse

joke_repository = JokeRepository(session=session)


def create_user(data: UserAuth):
    user = USERS.get(data.email)
    if user is not None:
        return JSONResponse(
            content={"message": f"User with {data.email} email already exist"},
            status_code=400)
    USERS[data.email] = {
        'email': data.email,
        'name': data.name,
        'quota': QUOTA,
        'password': get_hashed_password(data.password.get_secret_value()),
        'id': str(uuid4())
    }
    return JSONResponse(
        content={"message": "User added Successfully"},
        status_code=200)


def auth_user(username, password):
    user = USERS.get(username)
    if user and (user.get("password") == password):
        return True, generate_token(username)
    return False, "username or password is invalid"


def add_joke(joke: str, category: str):
    new_joke = Joke(body=joke, category=category)
    joke_repository.add(new_joke)
    return True


def get_random_joke(limit: int = 1):
    jokes = joke_repository.get_random_joke(limit)
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]


def search_joke(phrase: str, offset: int = 0, limit: int = 1):
    jokes = joke_repository.search(phrase=phrase, limit=limit, offset=offset)
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]


def get_joke_from_category(category: str, offset: int = 0, limit: int = 1):
    jokes = joke_repository.get_by_category(category=category.lower(),
                                            offset=offset, limit=limit)
    return [{"joke": joke.body, "category": joke.category} for joke in jokes]


def get_unapproved_jokes(offset: int, limit: int):
    kwargs = {"approved": False}
    jokes = joke_repository.get(offset=offset, limit=limit, kwargs=kwargs)
    return [{"joke": joke.body, "category": joke.category, "id": joke.id} for
            joke in jokes]


def approve_joke(_id: str):
    return joke_repository.approve(_id=_id)


def get_all_categories():
    categories = joke_repository.get_all_categories()
    return [category.tuple()[0] for category in categories]
