from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.repositories.incident_repository import IncidentRepository

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)

templates = Jinja2Templates(
    directory="backend/templates"
)


@router.get("/", response_class=HTMLResponse)
def incidents_page(
    request: Request,
    db: Session = Depends(get_db)
):

    incidents = IncidentRepository.get_all(db)

    return templates.TemplateResponse(
        request,
        "incidents.html",
        {
            "request": request,
            "incidents": incidents
        }
    )
    
@router.get("/{incident_id}", response_class=HTMLResponse)
def incident_details(
    incident_id: int,
    request: Request,
    db: Session = Depends(get_db)
):

    incident = IncidentRepository.get_by_id(
        db,
        incident_id
    )

    return templates.TemplateResponse(
        request,
        "incident_details.html",
        {
            "request": request,
            "incident": incident
        }
    )