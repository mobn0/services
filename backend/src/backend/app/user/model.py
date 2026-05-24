from backend.app.db.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, ForeignKey, UniqueConstraint

class Identity(Base):
    __tablename__ = "identity"

    __table_args__ = (
        UniqueConstraint("sub", "iss", name="uq_identity_sub_iss"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)
    sub: Mapped[str] = mapped_column(String(255), nullable=False)
    iss: Mapped[str] = mapped_column(String(255), nullable=False)

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True, unique=True, nullable=False)
    identity_id: Mapped[int] = mapped_column(Integer, ForeignKey("identity.id"), nullable=False, unique=True)
    

    identity: Mapped[Identity] = relationship("Identity", backref="user", uselist=False)