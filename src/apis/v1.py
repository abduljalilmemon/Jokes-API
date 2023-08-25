from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from utils import add_joke, get_random_joke, search_joke, get_joke_from_category, auth_user
from loguru import logger

v1 = APIRouter(prefix='/v1')


@v1.post("/user/login")
def user_sign(username: str, password: str):
    try:
        user, response = auth_user(username=username, password=password)
        if user:
            return JSONResponse(content=response, status_code=200)
        return JSONResponse(content=response, status_code=404)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@v1.get('/random')
def _get_random_joke():
    try:
        joke = get_random_joke()
        return JSONResponse(content=joke, status_code=200)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@v1.get('/lookup')
def get_lookup_joke(phrase: str):
    try:
        joke = search_joke(phrase=phrase)
        return JSONResponse(content=joke, status_code=200)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@v1.get('/category')
async def _get_joke_from_category(category: str, offset: int = 0,
                                  limit: int = 20):
    try:
        jokes = get_joke_from_category(category=category, offset=offset,
                                       limit=limit)
        if len(jokes) > 0:
            return JSONResponse(content=jokes, status_code=200)
        return JSONResponse(content=jokes, status_code=404)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@v1.post('/submit')
async def _add_joke(joke: str, category: str):
    try:
        add_joke(joke, category)
        return JSONResponse(status_code=200)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)
