from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, exists
from app.models.restaurant import Restaurant

async def restaurant_is_exist(db: AsyncSession, rest_id: int) -> bool:
    query = (
        select(exists()).
        where(Restaurant.id == rest_id, Restaurant.is_active.is_(True))
    )
    return bool(await db.scalar(query))