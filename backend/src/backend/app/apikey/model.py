from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from typing import TYPE_CHECKING
from backend.app.db.database import Base

if TYPE_CHECKING:
    from backend.app.user.model import User

class Apikey(Base):
    __tablename__ = "apikey"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)

    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="apikeys")