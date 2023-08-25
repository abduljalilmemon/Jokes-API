from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from auth.auth_bearer import JWTBearer
from utils import add_joke, get_random_joke, search_joke, \
    get_joke_from_category, auth_user, get_unapproved_jokes, approve_joke
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


@v1.get('/random', dependencies=[Depends(JWTBearer())])
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


@v1.get('/unapproved')
async def _get_unapproved_jokes(offset: int = 0, limit: int = 20):
    try:
        jokes = get_unapproved_jokes(offset=offset, limit=limit)
        if len(jokes) > 0:
            return JSONResponse(content=jokes, status_code=200)
        return JSONResponse(content=jokes, status_code=404)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@v1.post('/approve')
async def _approve_joke(joke_id: str):
    try:
        resp = approve_joke(_id=joke_id)
        if resp:
            return JSONResponse(content={"message": "joke approved successfully"},
                                status_code=200)
        return JSONResponse(content={"message": "No Joke Found"},
                            status_code=404)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@v1.post('/submit')
async def _add_joke(joke: str, category: str):
    try:
        add_joke(joke, category)
        return JSONResponse(content={"message": "joke added successfully"},
                            status_code=200)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)
