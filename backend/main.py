from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.api.routes import router
from backend.api.auth import router as auth_router

from backend.config.settings import settings
from backend.database.database import Base, engine

# Import models so SQLAlchemy creates the tables
from backend.models.user import User

app = FastAPI(
    title=settings.APP_NAME,
    description="Security Analyst Workbench",
    version=settings.VERSION
)

Base.metadata.create_all(bind=engine)

app.mount(
    "/static",
    StaticFiles(directory="backend/static"),
    name="static"
)

app.include_router(router)
app.include_router(auth_router)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.VERSION
    }