from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy import create_engine
from typing import AsyncGenerator
from .enviroment import env

POSTGRES_CREDENTIALS = f'{env.POSTGRES_USER}:{env.POSTGRES_PASSWORD}@{env.POSTGRES_HOST}:{env.POSTGRES_PORT}/{env.POSTGRES_DB}'
POSTGRES_CONNECTION = f'postgresql+asyncpg://{POSTGRES_CREDENTIALS}'

async_engine = create_async_engine(
    POSTGRES_CONNECTION,
    pool_size=20,
    pool_timeout=3000,
    max_overflow=0
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False
)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session