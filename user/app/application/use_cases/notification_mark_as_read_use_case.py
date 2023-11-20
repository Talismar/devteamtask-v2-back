from app.application.repositories.notification_repository import NotificationRepository
from app.domain.errors import BadRequestException, DatabaseException


class NotificationMarkAsReadUseCase:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    def execute(self, id: int):
        try:
            return self.notification_repository.mark_as_read(id)
        except DatabaseException:
            raise BadRequestException("Error creating notification")
