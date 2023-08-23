from fastapi import APIRouter
from fastapi.responses import JSONResponse
from utils import add_joke, get_random_joke
from loguru import logger

v1 = APIRouter(prefix='/v1')


@v1.get('/random')
def _get_random_joke():
    try:
        joke = get_random_joke()
        return JSONResponse(content=joke, status_code=200)
    except Exception as e:
        logger.error(e)
    return JSONResponse(status_code=500)


@v1.get('/lookup')
async def get_lookup_joke():
    return "TBD"


@v1.get('/category')
async def get_joke_from_category():
    return "TBD"


@v1.post('/submit')
async def _add_joke(joke: str, category: str):
    try:
        add_joke(joke, category)
        return JSONResponse(status_code=200)
    except Exception as e:
        logger.error(e)
    return JSONResponse(status_code=500)
