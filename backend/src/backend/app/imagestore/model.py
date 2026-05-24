from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String, UniqueConstraint
from uuid import uuid4
from typing import TYPE_CHECKING
from backend.app.db.database import Base

if TYPE_CHECKING:
    from backend.app.user.model import Apikey

class StoredImage(Base):
    __tablename__ = "storedimage"

    __table_args__ = (
        UniqueConstraint("name", "user_id", name="uq_storedimage_name_apikey_id"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)

    filename: Mapped[str] = mapped_column(String(255), nullable=False)

    stored_filename: Mapped[str] = mapped_column(String(36), nullable=False)

    apikey_id: Mapped[int] = mapped_column(
        ForeignKey("apikey.id"),
        nullable=False,
    )

    apikey: Mapped["Apikey"] = relationship(back_populates="storedimages")