from pydantic import BaseModel, ConfigDict
from backend.app.user.model import User

class Me(BaseModel):
    user: dict