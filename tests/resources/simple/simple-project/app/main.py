from fastapi import FastAPI

from app.api import router
from app.core.config import settings


def create_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)
    application.include_router(router)
    return application


app = create_application()
