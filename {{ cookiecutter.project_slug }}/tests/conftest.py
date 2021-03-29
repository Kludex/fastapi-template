import asyncio

import pytest
from dotenv import load_dotenv
from httpx import AsyncClient


load_dotenv(".env")

@pytest.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def client():
    from {{cookiecutter.package_name}}.main import app

    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client
