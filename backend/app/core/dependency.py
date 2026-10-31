from app.core.db import AsyncSessionName

async def get_db():
    async with AsyncSessionName() as session:
        yield session