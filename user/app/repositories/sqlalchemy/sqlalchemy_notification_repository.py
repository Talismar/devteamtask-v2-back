from app.models import NotificationModel
from app.repositories.notification_repository import NotificationRepository
from sqlalchemy.orm import Session


class SqlalchemyNotificationRepository(
    NotificationRepository[Session, NotificationModel]
):
    def create(self, data):
        instance = NotificationModel(**data)

        self._session.add(instance)
        self._session.commit()
        self._session.refresh(instance)

        return instance

    def mark_as_read(self, id: int) -> NotificationModel:
        notification_instance = (
            self._session.query(NotificationModel)
            .filter_by(id=id)
            .update({"state": False})
        )
        self._session.commit()

    def get_all_by_user_id(self, user_id: int) -> list[NotificationModel]:
        return (
            self._session.query(NotificationModel)
            .filter_by(user_id=user_id, state=True)
            .all()
        )
