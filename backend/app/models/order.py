from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, func
from app.core.db import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_item: Mapped[int] = mapped_column(ForeignKey("dishes.id"))
    table_id: Mapped[int] = mapped_column(ForeignKey("tables.id"))
    restaurant_id: Mapped[int] = mapped_column(ForeignKey("restaurants.id"))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    