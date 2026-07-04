from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.repositories.dashboard_repository import DashboardRepository

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

templates = Jinja2Templates(
    directory="backend/templates"
)



@router.get("/", response_class=HTMLResponse)
def dashboard(
    request: Request,
    db: Session = Depends(get_db)
):

    users = DashboardRepository.total_users(db)

    incidents = DashboardRepository.total_incidents(db)

    critical = DashboardRepository.critical_incidents(db)

    high = DashboardRepository.high_incidents(db)

    medium = DashboardRepository.medium_incidents(db)

    threat_score = min(
        critical * 40 +
        high * 20 +
        medium * 10,
        100
    )

    return templates.TemplateResponse(
        request,
        "dashboard.html",
        {
            "request": request,
            "users": users,
            "incidents": incidents,
            "critical": critical,
            "high": high,
            "medium": medium,
            "threat_score": threat_score
        }
    )