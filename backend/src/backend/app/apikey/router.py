# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from backend.app.dependencies import get_current_user, get_db

# router = APIRouter(prefix="/api", tags=["api"])

# @router.post("new")
# def create_api_key(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
