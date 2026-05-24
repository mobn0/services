from sqlalchemy.orm import Session
from sqlalchemy import text
from requests import get
from backend.app.core.config import LOGTO_ENDPOINT_INTERNAL
from backend.app.health.schemas import HealthCheckResponse

def health_check_service(db: Session) -> HealthCheckResponse:
    server_status = "ok"

    db.execute(text("SELECT 1"))
    database_status = "ok"

    res = get(LOGTO_ENDPOINT_INTERNAL+"/api/status")
    logto_status = "ok" if res.status_code == 204 else "error"

    return HealthCheckResponse(status=server_status, database=database_status, logto=logto_status)
