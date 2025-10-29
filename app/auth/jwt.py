import jwt, datatime
from typing import Optional
from app.core.config import settings

ALGO = "HS256"

def create_token(sub: str) -> str:
    exp = datatime.datatime.utcnow() + datatime.timedelta(minutes=settings.jwt_expire_minutes)
    payload = {"sub": sub, "exp" : exp}
    return jwt.encode(payload, settings.jwt_secret, algorithm=ALGO)

def decode_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, settings.jwt_secret, algorithm =[ALGO])
    except jwt.PyJWTError:
        return None
