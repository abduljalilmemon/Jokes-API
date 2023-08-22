from fastapi import APIRouter
from utils import add_joke

v1 = APIRouter(prefix='/v1')


@v1.get('/random')
async def get_random_joke():
    return "TBD"


@v1.get('/lookup')
async def get_lookup_joke():
    return "TBD"


@v1.get('/category')
async def get_joke_from_category():
    return "TBD"


@v1.post('/submit')
async def _add_joke(joke: str, category: str):
    add_joke(joke, category)
    return True
