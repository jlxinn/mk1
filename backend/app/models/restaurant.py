from sqlalchemy.orm import Mapped, mapped_column
from uuid import uuid4
from app.core.db import Base
from sqlalchemy import ForeignKey, func, String, DateTime, UniqueConstraint
from datetime import datetime

class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    api_key_hash: Mapped[str] = mapped_column(String(64), unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
        )


class Table(Base):
    __tablename__ = "tables"
    __table_args__ = (UniqueConstraint("restaurant_id", "number"),)   

    id: Mapped[int] = mapped_column(primary_key=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"), index=True)
    number: Mapped[int]
    qr_token: Mapped[str] = mapped_column(
        String(36), unique=True, default=lambda: str(uuid4())
    )
    is_active: Mapped[bool] = mapped_column(default=True)