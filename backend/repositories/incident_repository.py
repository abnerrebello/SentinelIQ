from sqlalchemy.orm import Session

from backend.models.incident import Incident


class IncidentRepository:

    @staticmethod
    def create(db: Session, incident: Incident):

        db.add(incident)

        db.commit()

        db.refresh(incident)

        return incident

    @staticmethod
    def get_all(db: Session):

        return db.query(Incident).all()

    @staticmethod
    def delete_all(db: Session):

        db.query(Incident).delete()

        db.commit()
    
    @staticmethod
    def get_by_id(db: Session, incident_id: int):

        return db.query(Incident).filter(
            Incident.id == incident_id
        ).first()