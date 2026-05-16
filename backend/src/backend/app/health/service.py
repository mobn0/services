from sqlalchemy.orm import Session
from sqlalchemy import text
from backend.app.health.schemas import HealthCheckResponse

def health_check(db: Session):
    server_status = "ok"

    db.execute(text("SELECT 1"))
    database_status = "ok"
    
    return HealthCheckResponse(status=server_status, database=database_status)
