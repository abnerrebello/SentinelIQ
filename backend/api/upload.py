from fastapi import APIRouter, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import os
import shutil

from backend.parser.csv_parser import CSVParser
from backend.detection.rule_engine import RuleEngine
from backend.database.database import SessionLocal
from backend.models.incident import Incident
from backend.repositories.incident_repository import IncidentRepository

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

templates = Jinja2Templates(
    directory="backend/templates"
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.get("/", response_class=HTMLResponse)
def upload_page(request: Request):

    return templates.TemplateResponse(
        request,
        "upload.html",
        {
            "request": request
        }
    )


@router.post("/")
async def upload_file(file: UploadFile = File(...)):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Parse CSV
    events = CSVParser.parse(filepath)

    # Detect attacks
    alerts = RuleEngine.detect(events)

    # Save incidents to database
    db = SessionLocal()

    try:
        IncidentRepository.delete_all(db)

        for alert in alerts:
            incident = Incident(
        incident_type=alert["type"],
        severity=alert["severity"],
        ip=alert["ip"],
        failed_attempts=alert["failed_attempts"],
        mitre_id=alert["mitre_id"],
        mitre_name=alert["mitre_name"]
        )

            IncidentRepository.create(db, incident)

    finally:
        db.close()

    return {
        "message": "Upload Successful",
        "filename": file.filename,
        "total_events": len(events),
        "alerts": alerts,
        "events": events
    }