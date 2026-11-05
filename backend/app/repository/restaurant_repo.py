from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.restaurant import Restaurant

async def restaurant_is_exist(db: AsyncSession, rest_id: int) -> bool:
    query = (
        select(Restaurant).
        where(Restaurant.id == rest_id)
    )

    return query