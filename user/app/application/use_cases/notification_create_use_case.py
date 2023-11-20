from app.application.dtos import NotificationCreateRequestDTO
from app.application.repositories.notification_repository import NotificationRepository
from app.domain.errors import BadRequestException, DatabaseException


class NotificationCreateUseCase:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository

    def execute(self, data: NotificationCreateRequestDTO):
        try:
            return self.notification_repository.create(data)
        except DatabaseException:
            raise BadRequestException("Error creating notification")
