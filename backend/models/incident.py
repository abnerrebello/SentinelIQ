from sqlalchemy import Column, Integer, String

from backend.database.database import Base


class Incident(Base):

    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)

    incident_type = Column(String, nullable=False)

    severity = Column(String, nullable=False)

    ip = Column(String, nullable=False)

    failed_attempts = Column(Integer, default=0)

    status = Column(String, default="Open")

    mitre_id = Column(String, default="")

    mitre_name = Column(String, default="")