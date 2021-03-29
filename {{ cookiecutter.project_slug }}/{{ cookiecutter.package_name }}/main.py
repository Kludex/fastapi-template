from fastapi import FastAPI
{% if cookiecutter.add_cors == 'True' -%}
from fastapi.middleware.cors import CORSMiddleware
{% endif %}

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
    {% if cookiecutter.add_cors == 'True' -%}
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    {% endif %}
    application.include_router(router)
    return application


app = create_application()
