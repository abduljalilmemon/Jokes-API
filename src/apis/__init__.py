from fastapi import APIRouter
from .v1 import v1
__all__ = ["api"]
api = APIRouter(prefix='/jokes')
api.include_router(v1)
