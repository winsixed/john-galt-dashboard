from fastapi import Depends, HTTPException, status
from functools import wraps
from app.auth.dependencies import get_current_user

def has_permission(permission_name: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(current_user=Depends(get_current_user), *args, **kwargs):
            perms = {p.name for p in current_user.role.permissions}
            if permission_name not in perms:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
            return await func(*args, **kwargs)
        return wrapper
    return decorator
