from sqlalchemy import text
from src.models import metadata_obj
from src.database import engine

async def get_conn_res():
    async with engine.connect() as conn:
        res = await conn.execute(text('SELECT VERSION()'))
        print(f'{res.first()=}')
        await conn.commit()


async def create_tables():
    # await metadata_obj.create_all(engine)
    async with engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all)