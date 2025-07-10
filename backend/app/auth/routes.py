from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import User
from app.auth.jwt import create_tokens, decode_token
from app.auth.schemas import LoginIn, Token
from app.auth.utils import verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=data.username).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access, refresh = create_tokens(user.id)
    return {"access_token": access, "refresh_token": refresh}

@router.post("/refresh", response_model=Token)
def refresh(token: str):
    payload = decode_token(token)
    access, refresh = create_tokens(int(payload["sub"]))
    return {"access_token": access, "refresh_token": refresh}
