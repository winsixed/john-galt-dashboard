from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import User
from app.schemas.user import UserCreate, UserOut
from app.auth.decorators import has_permission
from app.auth.utils import hash_password

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserOut])
@has_permission("view_users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/", response_model=UserOut)
@has_permission("create_users")
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    hashed = hash_password(data.password)
    user = User(username=data.username, hashed_password=hashed, role_id=data.role_id)
    db.add(user); db.commit(); db.refresh(user)
    return user

@router.put("/{user_id}", response_model=UserOut)
@has_permission("edit_users")
def update_user(user_id: int, data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    user.username, user.hashed_password, user.role_id = data.username, hash_password(data.password), data.role_id
    db.commit(); db.refresh(user)
    return user

@router.delete("/{user_id}")
@has_permission("delete_users")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db.delete(db.query(User).get(user_id)); db.commit()
    return {"msg": "Deleted"}
