from fastapi import FastAPI

from docker_project.api import router
from docker_project.core.config import settings


def create_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)
    application.include_router(router)
    return application


app = create_application()
