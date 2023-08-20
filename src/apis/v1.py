from fastapi import APIRouter

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


@v1.get('/submit')
async def add_joke():
    return "TBD"
