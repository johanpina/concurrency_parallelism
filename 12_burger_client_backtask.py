import httpx
import asyncio
import time

async def make_order(path: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'http://127.0.0.1:8000{path}')
        print(response.json())

async def main():
    t0 = time.time()
    orders = [
        "/order/burgers/2",
        "/order/drinks/coke",
        "/order/burgers/3",
        "/order/drinks/water",
        "/order/burgers/1",
        "/order/drinks/lemonade"
    ]
    tasks = [make_order(order) for order in orders]
    await asyncio.gather(*tasks)
    elapsed = time.time() - t0
    print(f"Orders took {elapsed:.2f} seconds")

if __name__ == '__main__':
    asyncio.run(main())
