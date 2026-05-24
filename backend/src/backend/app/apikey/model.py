from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String, Text, UniqueConstraint
from typing import TYPE_CHECKING
from backend.app.db.database import Base

if TYPE_CHECKING:
    from backend.app.imagestore.model import StoredImage
    from backend.app.user.model import User

class Apikey(Base):
    __tablename__ = "apikey"

    __table_args__ = (
        UniqueConstraint("name", "user_id", name="uq_apikey_name_user_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    description: Mapped[str] = mapped_column(Text, nullable=False)

    prefix: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)

    secret: Mapped[str] = mapped_column(String(96), nullable=False, unique=True)
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="apikeys")

    
    storedimages: Mapped[list["StoredImage"]] = relationship(
        back_populates="apikey",
        cascade="all, delete-orphan",
    )