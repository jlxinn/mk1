from app.models.dish import Category, Dish 
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select


async def get_menu(db: AsyncSession, restaurant_id: int) -> list[Category]:
    query = (
        select(Category)
        .where(Category.restaurant_id == restaurant_id)
        .options(selectinload(Category.dishes.and_(Dish.is_active.is_(True))))
        .order_by(Category.sort_order, Category.id)
    )

    result = await db.execute(query)
    categories = result.scalars().all()

    return list(categories)
