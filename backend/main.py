from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.api.upload import router as upload_router
from backend.api.routes import router
from backend.api.auth import router as auth_router
from backend.api.dashboard import router as dashboard_router
from backend.api.incidents import router as incidents_router
from backend.config.settings import settings
from backend.database.database import Base, engine
from backend.models.incident import Incident
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
app.include_router(dashboard_router)
app.include_router(upload_router)
app.include_router(incidents_router)

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "version": settings.VERSION
    }