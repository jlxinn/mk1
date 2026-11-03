from app.models import dish 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select


async def get_menu(db: AsyncSession, restaurant_id: int,):
    query = (
        select(dish.Category)
        .where(dish.Category.restaurant_id == restaurant_id)
        .options(selectinload(dish.Category.dishes))
        .order_by(dish.Category.sort_order)
    )

    result = await db.execute(query)
    categories = result.scalars().all()

    return categories