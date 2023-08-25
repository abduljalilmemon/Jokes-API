from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from auth.auth_bearer import JWTBearer
from utils import get_random_joke, search_joke, get_joke_from_category, \
    get_unapproved_jokes, approve_joke
from loguru import logger

premium = APIRouter(prefix='/premium')


@premium.get('/random', dependencies=[Depends(JWTBearer())])
def _get_random_joke():
    try:
        joke = get_random_joke(limit=20)
        if len(joke) > 0:
            return JSONResponse(content=joke, status_code=200)
        return JSONResponse(content=joke, status_code=404)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@premium.get('/lookup', dependencies=[Depends(JWTBearer())])
def get_lookup_joke(phrase: str, offset: int = 0, limit: int = 20):
    try:
        joke = search_joke(phrase=phrase, offset=offset, limit=limit)
        if len(joke) > 0:
            return JSONResponse(content=joke, status_code=200)
        return JSONResponse(content=joke, status_code=404)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@premium.get('/category', dependencies=[Depends(JWTBearer())])
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


@premium.get('/unapproved', dependencies=[Depends(JWTBearer())])
async def _get_unapproved_jokes(offset: int = 0, limit: int = 20):
    try:
        jokes = get_unapproved_jokes(offset=offset, limit=limit)
        if len(jokes) > 0:
            return JSONResponse(content=jokes, status_code=200)
        return JSONResponse(content=jokes, status_code=404)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)


@premium.post('/approve', dependencies=[Depends(JWTBearer())])
async def _approve_joke(joke_id: str):
    try:
        resp = approve_joke(_id=joke_id)
        if resp:
            return JSONResponse(
                content={"message": "joke approved successfully"},
                status_code=200)
        return JSONResponse(content={"message": "No Joke Found"},
                            status_code=404)
    except Exception as e:
        logger.error(e)
    return JSONResponse(content={}, status_code=500)
