from fastapi import FastAPI

from postgres_docker_project.api import router
from postgres_docker_project.core.config import settings


def create_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)
    application.include_router(router)
    return application


app = create_application()
