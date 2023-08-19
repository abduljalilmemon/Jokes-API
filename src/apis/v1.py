from fastapi import APIRouter

v1 = APIRouter(prefix='/v1')


@v1.get('/get_random_joke')
async def get_random_joke():
    return "TBD"
