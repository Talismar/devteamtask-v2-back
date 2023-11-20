from app.application.repositories.notification_repository import NotificationRepository
from app.domain.errors import BadRequestException, DatabaseException


class NotificationGetAllActiveByUserUseCase:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    def execute(self, user_id: int):
        try:
            return self.notification_repository.get_all_by_user_id(user_id)
        except DatabaseException:
            raise BadRequestException("Database exception")
