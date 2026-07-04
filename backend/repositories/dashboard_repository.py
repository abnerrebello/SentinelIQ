from sqlalchemy.orm import Session

from backend.models.user import User
from backend.models.incident import Incident


class DashboardRepository:

    @staticmethod
    def total_users(db: Session):
        return db.query(User).count()

    @staticmethod
    def total_incidents(db: Session):
        return db.query(Incident).count()

    @staticmethod
    def critical_incidents(db: Session):
        return db.query(Incident).filter(
            Incident.severity == "Critical"
        ).count()

    @staticmethod
    def high_incidents(db: Session):
        return db.query(Incident).filter(
            Incident.severity == "High"
        ).count()

    @staticmethod
    def medium_incidents(db: Session):
        return db.query(Incident).filter(
            Incident.severity == "Medium"
        ).count()