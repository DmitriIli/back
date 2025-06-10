import asyncio
from src.queries.core import get_conn_res
from src.queries.core import create_tables

async def main():
    # await get_conn_res()
    await create_tables()


if __name__ == '__main__':

    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # try:
    #     # asyncio.run(get_conn_res())
    #     asyncio.run(create_tables())
    # except KeyboardInterrupt:
    #     pass

    asyncio.run(main())