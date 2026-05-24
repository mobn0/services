from fastapi import APIRouter, Depends
from backend.app.dependencies import get_current_user
from backend.app.user.schemas import Me
from backend.app.user.service import get_me

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/me", response_model=Me)
def me(current_user: dict = Depends(get_current_user)) -> Me:
    return get_me(current_user)
