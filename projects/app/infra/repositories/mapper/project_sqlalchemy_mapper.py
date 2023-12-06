from app.domain.entities.project import Project
from app.infra.database.models import ProjectModel

from .task_sqlalchemy_mapper import TaskSqlalchemyMapper


class ProjectSqlalchemyMapper:
    @staticmethod
    def toDomain(raw: ProjectModel) -> Project:
        return {
            "id": raw.id,
            "name": raw.name,
            "state": raw.state,  # type: ignore
            "end_date": raw.end_date,
            "start_date": raw.start_date,
            "logo_url": raw.logo_url,
            "leader_id": raw.leader_id,
            "product_owner_id": raw.product_owner_id,
            "collaborators_ids": set(row.user_id for row in raw.collaborators_ids),
            "status": [
                {"id": row.id, "name": row.name}
                for row in sorted(raw.status, key=lambda status: status.id)
            ],
            "tags": [{"id": row.id, "name": row.name} for row in raw.tags],
            "tasks": [TaskSqlalchemyMapper.toDomain(row) for row in raw.tasks],
            "sprints": [
                {
                    "id": row.id,
                    "name": row.name,
                    "description": row.description,
                    "project_id": row.project_id,
                    "state": row.state,
                    "created_at": row.created_at,
                    "updated_at": row.updated_at,
                }
                for row in raw.sprints
            ],
        }

    @staticmethod
    def toListDomain(raw: ProjectModel) -> Project:
        return {
            "id": raw.id,
            "name": raw.name,
            "state": raw.state,  # type: ignore
            "end_date": raw.end_date,
            "start_date": raw.start_date,
            "logo_url": raw.logo_url,
            "leader_id": raw.leader_id,
            "product_owner_id": raw.product_owner_id,
            "collaborators_ids": set(row.user_id for row in raw.collaborators_ids),
            "sprints": [
                {
                    "id": row.id,
                    "name": row.name,
                    "description": row.description,
                    "project_id": row.project_id,
                    "state": row.state,
                    "created_at": row.created_at,
                    "updated_at": row.updated_at,
                }
                for row in raw.sprints
            ],
        }
