import asyncio
import time

async def say(i):
    await asyncio.sleep(i)

async def main():
    task1 = asyncio.create_task(say(1))
    task2 = asyncio.create_task(say(3))
    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"over time{time.strftime('%X')}")

# asyncio.run(main())
async def nested():
    return 42
