from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.dependencies import get_current_user, get_db
from backend.app.apikey.schema import ApikeyCreateResponse, ApikeyCreate
from backend.app.apikey.service import create_api_key_service

router = APIRouter(prefix="/apikey", tags=["apikey"])

@router.post("/create", response_model=ApikeyCreateResponse)
async def create_api_key(params: ApikeyCreate, current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    return create_api_key_service(params.name, params.description, current_user, db)