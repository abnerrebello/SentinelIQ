from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.routes import router

from backend.config.settings import settings
from backend.database.database import Base, engine
from backend.models.user import User

app = FastAPI(
    title=settings.APP_NAME,
    description="Security Analyst Workbench",
    version=settings.VERSION
)

app.mount(
    "/static",
    StaticFiles(directory="backend/static"),
    name="static"
)
Base.metadata.create_all(bind=engine)

app.include_router(router)