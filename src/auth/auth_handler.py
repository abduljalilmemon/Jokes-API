import time
import jwt
from config import JWT_SECRET, JWT_ALGORITHM


def generate_token(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + 300
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}


def decode_token(token: str):
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return decoded_token if decoded_token.get("expires", (
                time.time() + 10)) >= time.time() else None
