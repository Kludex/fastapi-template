import asyncio
{%- if cookiecutter.database == "PostgreSQL" %}
import os
{%- endif %}

import pytest
from asgi_lifespan import LifespanManager
from dotenv import load_dotenv
from httpx import AsyncClient

load_dotenv(".env")
{%- if cookiecutter.database == "PostgreSQL" %}
os.environ["POSTGRES_HOST"] = "localhost"
os.environ["POSTGRES_DB"] = "test"


@pytest.fixture(autouse=True)
async def connection():
    from {{cookiecutter.package_name}}.core.database import engine

    async with engine.begin() as conn:
        yield conn
        await conn.rollback()

{%- endif %}


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def client():
    from {{cookiecutter.package_name}}.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac, LifespanManager(app):
        yield ac
