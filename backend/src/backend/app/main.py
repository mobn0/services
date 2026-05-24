from fastapi import FastAPI
from backend.app.health.router import router as health_router
from backend.app.user.router import router as user_router

app = FastAPI()

app.include_router(health_router)
app.include_router(user_router)