from abc import ABC, abstractmethod

from app.application.dtos import NotificationCreateRequestDTO
from app.domain.entities.notification import Notification


class NotificationRepository(ABC):
    @abstractmethod
    def create(self, data: NotificationCreateRequestDTO) -> Notification:
        pass

    @abstractmethod
    def mark_as_read(self, id: int):
        pass

    @abstractmethod
    def get_all_by_user_id(self, user_id: int) -> list[Notification]:
        pass
