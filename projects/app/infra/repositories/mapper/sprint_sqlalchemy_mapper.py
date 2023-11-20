from app.domain.entities.sprint import Sprint
from app.infra.database.models import SprintModel


class SprintSqlalchemyMapper:
    @staticmethod
    def toDomain(raw: SprintModel) -> Sprint:
        return {
            "id": raw.id,
            "name": raw.name,
            "description": raw.description,
            "project_id": raw.project_id,
            "state": raw.state,  # type: ignore
            "created_at": raw.created_at,
            "updated_at": raw.updated_at,
        }
