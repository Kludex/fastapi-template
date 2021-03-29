from fastapi import FastAPI

from {{cookiecutter.package_name}}.api import router
from {{cookiecutter.package_name}}.core.config import settings


def create_application() -> FastAPI:
{%- if cookiecutter.docstring == 'Google' %}
    """Wrapper function to create a FastAPI application.

    Returns:
        FastAPI: Newly created FastAPI application.
    """
{% endif %}
    application = FastAPI(title=settings.PROJECT_NAME)
    application.include_router(router)
    return application


app = create_application()
