from fastapi import FastAPI

from {{cookiecutter.package_name}}.api import router


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application


app = create_application()
