from decimal import Decimal
from pydantic import BaseModel

class DishResponse(BaseModel):
    id: int
    name: str
    price: Decimal
    is_active: bool

    class Config:
        from_attributes = True

class CategoryResponse(BaseModel):
    id: int
    name: str
    sort_order: int
    dishes: list[DishResponse] = []

    class Config:
        from_attributes = True