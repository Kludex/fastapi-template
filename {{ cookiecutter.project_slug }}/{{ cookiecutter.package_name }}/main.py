from fastapi import FastAPI

from {{cookiecutter.package_name}}.api import router


def create_application() -> FastAPI:
{%- if cookiecutter.docstring == 'Google' %}
    """Wrapper function to create a FastAPI application.

    Returns:
        FastAPI: Newly created FastAPI application.
    """
{% endif %}
    application = FastAPI()
    application.include_router(router)
    return application


app = create_application()
