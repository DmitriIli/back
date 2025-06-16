from sqlalchemy import text, insert
from src.models import metadata_obj, Users
from src.database import engine, async_session_factory
from src.models import Base


async def get_conn_res():
    async with engine.connect() as conn:
        res = await conn.execute(text('SELECT VERSION()'))
        print(f'{res.first()=}')
        await conn.commit()


async def create_tables():
    engine.echo = True
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    engine.echo = True




async def insert_data():
    user1 = Users(username='user1')
    async with async_session_factory() as session:
        session.add(user1)
        await session.commit()
        
# async def insert_data():
#     async with engine.connect() as conn:
#         # stmn = """ INSERT INTO users (name) VALUES
#         # ('name1'),
#         # ('name2'); """
#         stmn = insert(users_table).values(
#             [
#                 {'name':'name1'},
#                 {'name':'name2'}
#             ]

#         )
#         # await conn.execute(text(stmn))
#         await conn.execute(stmn)
#         await conn.commit()