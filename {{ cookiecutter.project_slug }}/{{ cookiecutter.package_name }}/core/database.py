from typing import Any, AsyncGenerator, Dict

from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker

from {{ cookiecutter.package_name }}.core.config import settings

engine = create_async_engine(settings.POSTGRES_URI, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@as_declarative()
class Base:
    def dict(self) -> Dict[str, Any]:
        {%- if cookiecutter.docstring == 'Google' %}
        """Convert database row into a dictionary.

        Returns:
            Dict[str, Any]: Row's dictionary.
        """
        {% endif %}
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    {%- if cookiecutter.docstring == 'Google' %}
    """Gets a database session."""
    {% endif %}
    async with SessionLocal() as session:
        yield session
