from datetime import datetime, timedelta
from typing import Tuple
import jwt
from app.config import Settings

settings = Settings()

def create_tokens(user_id: int) -> Tuple[str, str]:
    now = datetime.utcnow()
    access_payload = {"sub": str(user_id), "exp": now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)}
    refresh_payload = {"sub": str(user_id), "exp": now + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)}
    access = jwt.encode(access_payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    refresh = jwt.encode(refresh_payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return access, refresh

def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
