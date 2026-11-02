from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, Numeric, UniqueConstraint
from app.core.db import Base
from decimal import Decimal


class Category(Base):
    __tablename__ = "categories"
    __table_args__ = (UniqueConstraint("restaurant_id", "name"),)   

    id: Mapped[int] = mapped_column(primary_key=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"), index=True)
    name: Mapped[str] = mapped_column(String(50))
    sort_order: Mapped[int] = mapped_column(default=0)

class Dish(Base):
    __tablename__="dishes"
    __table_args__ = (UniqueConstraint("restaurant_id", "external_id"),)  

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="RESTRICT"), index=True)
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id", ondelete="RESTRICT"), index=True)
    external_id: Mapped[str | None] = mapped_column(String(64))
    name: Mapped[str] = mapped_column(String(127))
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    is_active: Mapped[bool] = mapped_column(default=True)