from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from app.core.db import Base
from decimal import Decimal


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    dish_id: Mapped[int] = mapped_column(ForeignKey("dish.id"), nullable=False)


class Dish(Base):
    __tablename__="dishes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(127), nullable=False)
    price: Mapped[Decimal] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("cotegories.id"))
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"))
    is_active: Mapped[bool] = mapped_column(default=True)