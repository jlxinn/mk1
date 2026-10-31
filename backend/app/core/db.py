from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

connect_args = (
    {"check_same_threads": False} if "sqlite" in settings.DATABASE_URL else {}
)

engine = create_async_engine(
    settings.DATABASE_URL, echo=True, connect_args=connect_args
)

AsyncSessionName = async_sessionmaker (
    engine, expire_on_commit=False, autoflush=False
)

class Base(DeclarativeBase):
    pass

    