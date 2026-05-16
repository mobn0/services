from fastapi import FastAPI
from backend.app.health.router import router as health_router

app = FastAPI()

app.include_router(health_router)