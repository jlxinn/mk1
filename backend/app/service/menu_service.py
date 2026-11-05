from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.repository.menu_repo import get_menu as repo_get_menu
from app.repository.restaurant_repo import restaurant_is_exist as repo_rest_is_exist
from app.schemas.dish import CategoryResponse

async def get_rest_menu_service(db: AsyncSession, rest_id: int) -> list[CategoryResponse]:

    if not await repo_rest_is_exist(db, rest_id):
        raise HTTPException(status_code=404, detail="Ресторан не найден")

    categories = await repo_get_menu(db, rest_id)

    return [CategoryResponse.model_validate(cat) for cat in categories]