from fastapi import FastAPI
from app.api.v1.menu import router as menu_router


app = FastAPI(title="Qr in Bishkek Babe")

app.include_router(menu_router, prefix="/api/v1", tags=['Menu'])