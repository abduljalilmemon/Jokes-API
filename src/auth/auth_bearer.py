from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .auth_handler import decode_token, get_token_user_id
from loguru import logger
from config import USERS


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer,
                                                                self).__call__(
            request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403,
                                    detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403,
                                    detail="Invalid token or expired token.")
            quota = self.consume_quota(credentials.credentials)
            if quota < 0:
                raise HTTPException(status_code=403,
                                    detail="Token valid, quota expired")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403,
                                detail="Invalid authorization code.")

    @staticmethod
    def verify_jwt(token: str) -> bool:
        try:
            payload = decode_token(token)
            return True if payload else False
        except Exception as e:
            logger.warning(e)
        return False

    @staticmethod
    def consume_quota(token):
        email = get_token_user_id(token)
        user = USERS.get(email)
        user["quota"] = user.get("quota", 0) - 1
        return user.get("quota")
