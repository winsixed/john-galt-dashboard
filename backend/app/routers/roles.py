from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import Role
from app.auth.decorators import has_permission

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("/", response_model=list[dict])
@has_permission("view_roles")
def get_roles(db: Session = Depends(get_db)):
    roles = db.query(Role).all()
    return [{"id": r.id, "name": r.name} for r in roles]
