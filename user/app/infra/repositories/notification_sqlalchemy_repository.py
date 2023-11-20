from app.application.repositories import NotificationRepository
from app.domain.errors import DatabaseException, ResourceNotFoundException
from app.infra.database import NotificationModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .mapper.notification_sqlalchemy_mapper import NotificationSqlalchemyMapper


class NotificationSqlalchemyRepository(NotificationRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, data):
        instance = NotificationModel(**data)

        try:
            self.session.add(instance)
            self.session.commit()
            self.session.refresh(instance)
        except IntegrityError:
            raise DatabaseException("Could not create instance")

        return NotificationSqlalchemyMapper.toDomain(instance)

    def mark_as_read(self, id):
        notification = self.session.query(NotificationModel).filter_by(id=id).first()

        if notification is None:
            raise ResourceNotFoundException("Notification")

        notification.state = False

        self.session.commit()
        self.session.refresh(notification)

        return NotificationSqlalchemyMapper.toDomain(notification)

    def get_all_by_user_id(self, user_id):
        notification_models = (
            self.session.query(NotificationModel)
            .filter_by(user_id=user_id, state=True)
            .all()
        )
        return [
            NotificationSqlalchemyMapper.toDomain(row) for row in notification_models
        ]
