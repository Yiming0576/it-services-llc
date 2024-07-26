import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(say_after(10, 'Hello'))
    task2 = asyncio.create_task(say_after(3, 'World'))

    print("Starting tasks")
    await task1
    await task2

asyncio.run(main())
