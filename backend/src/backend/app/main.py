from fastapi import FastAPI
from contextlib import asynccontextmanager
from backend.app.health.router import router as health_router
from backend.app.user.router import router as user_router
from backend.app.db.database import init_db
from backend.app.user.model import User, Identity
from backend.app.apikey.model import Apikey

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(health_router)
app.include_router(user_router)

    