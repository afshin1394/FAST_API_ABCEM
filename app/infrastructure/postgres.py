import logging
from keyword import kwlist

from abcem.app.core.config import settings
from fastapi import logger
from abcem.app.infrastructure.schemas.base_db_model import  Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine



DATABASE_URL = f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"  # Replace with your database URL

def get_async_engine() -> AsyncEngine:
    """Return async database engine."""
    try:
        async_engine: AsyncEngine = create_async_engine(

            future=True,
            url=DATABASE_URL
        )
        return async_engine
    except SQLAlchemyError as e:
        logger.logger.warning("Unable to establish db engine, database might not exist yet")
        logger.logger.warning(e)



async def initialize_database() -> None:
    """Create table in metadata if they don't exist yet.

    This uses a sync connection because the 'create_all' doesn't
    feature async yet.
    """
    async_engine = get_async_engine()
    async with async_engine.begin() as async_conn:
        await async_conn.run_sync(Base.metadata.create_all)
        logger.logger.log(msg="Initializing database was successfull.",level=logging.INFO)









