from app.domain.entities.task import Task
from app.infra.database.models import TaskModel


class TaskSqlalchemyMapper:
    @staticmethod
    def toDomain(raw: TaskModel) -> Task:
        return {
            "id": raw.id,
            "name": raw.name,
            "description": raw.description,
            "assigned_to_user_id": raw.assigned_to_user_id,
            "created_by_user_id": raw.created_by_user_id,
            "priority": raw.priority,
            "sprint_id": raw.sprint_id,
            "created_at": raw.created_at,
            "updated_at": raw.updated_at,
            "status": {"id": raw.status.id, "name": raw.status.name},
            "tags": [{"id": row.id, "name": row.name} for row in raw.tags],
        }
