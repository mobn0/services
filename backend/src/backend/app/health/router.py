from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.dependencies import get_db
from backend.app.health.schemas import HealthCheckResponse
from backend.app.health.service import health_check

router = APIRouter(prefix="/health", tags=["health"])

@router.post("/", response_model=HealthCheckResponse)
def get_health_check(db: Session = Depends(get_db)) -> HealthCheckResponse:
    return health_check(db)