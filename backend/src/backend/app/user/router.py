from fastapi import APIRouter, Depends
from backend.app.dependencies import get_current_user
from backend.app.user.schemas import Me
from backend.app.user.service import me_service
from backend.app.user.model import User

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/me", response_model=Me)
async def me(current_user: User = Depends(get_current_user)) -> Me:
    return me_service(current_user)
