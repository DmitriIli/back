import asyncio
from src.queries.orm import AsyncORM


async def main():
    # task1 = asyncio.create_task(AsyncORM.create_table())
    task2 = asyncio.create_task(AsyncORM.insert_data())
    # await task1
  
    await task2


if __name__ == '__main__':

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
