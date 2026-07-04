from pydantic import BaseModel


class IncidentResponse(BaseModel):

    id: int

    incident_type: str

    severity: str

    ip: str

    failed_attempts: int

    status: str

    class Config:
        from_attributes = True