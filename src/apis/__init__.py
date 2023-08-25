from fastapi import APIRouter
from .v1 import v1
from .internal import internal
from .premium import premium
__all__ = ["api"]
api = APIRouter(prefix='/jokes')
api.include_router(v1)
api.include_router(internal)
api.include_router(premium)
