from app.domain.entities.notification import Notification
from app.infra.database import NotificationModel


class NotificationSqlalchemyMapper:
    @staticmethod
    def toDomain(raw: NotificationModel) -> Notification:
        return {
            "id": raw.id,
            "title": raw.title,
            "description": raw.description,
            "user_id": raw.user_id,
            "state": raw.state,
            "created_at": raw.created_at,
            "updated_at": raw.updated_at,
        }

    @staticmethod
    def toSqlAlchemy(data: Notification):
        return NotificationModel(**data)
