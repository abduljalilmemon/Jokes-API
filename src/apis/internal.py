from fastapi import APIRouter
from migrations.json_to_mysql import json_to_mysql
from loguru import logger

internal = APIRouter(prefix='/internal')


@internal.get('migrate/json_to_mysql')
async def migrate_json_to_mysql():
    try:
        json_to_mysql()
        return True
    except Exception as e:
        logger.error(e)
    return False
