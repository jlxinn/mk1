from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field

class DishResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: Decimal

class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    sort_order: int
    dishes: list[DishResponse] = Field(default_factory=list)
    