import asyncio
from sqlalchemy import text, insert
from src.models import Users, Base
from src.database import engine, async_session_factory


class AsyncORM:

    @staticmethod
    async def create_table():
        async with engine.begin() as conn:
            engine.echo = False
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            engine.echo = False

    @staticmethod
    async def insert_data():
        async with async_session_factory() as session:
            user1 = Users(username='user1')
            session.add(user1)
            await session.flush()
            await session.commit()
