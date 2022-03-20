import asyncio as aio

import httpx
from urlpath import URL

BASE_URL = URL("http://192.168.1.6:8080")
TARGET_URL = str(BASE_URL / "api" / "card") + "/"
SLEEP_TIME = 0.1
CLIENTS = 255


async def dummy_client(client_id: int):
    async with httpx.AsyncClient() as client:
        while True:
            resp = await client.get(TARGET_URL)
            print(f"Client {client_id} {TARGET_URL}: {resp.status_code}")
            await aio.sleep(SLEEP_TIME)


async def main():
    for i in range(CLIENTS):
        aio.create_task(dummy_client(i))

    while True:
        await aio.sleep(0.1)


if __name__ == "__main__":
    aio.run(main())
