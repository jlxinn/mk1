from fastapi import APIRouter, Depends
from app.core.dependency import get_db
from sqlalchemy.ext.asyncio import AsyncSession

from app.service.menu_service import get_rest_menu_service

from app.schemas.dish import CategoryResponse 


router = APIRouter()

@router.get("/restaurants/{restaurant_id}/menu", response_model=list[CategoryResponse])
async def get_menu(restaurant_id: int, db:AsyncSession = Depends(get_db)):
    return await get_rest_menu_service(db, restaurant_id)