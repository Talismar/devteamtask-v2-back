from typing import TypedDict

from app.repositories.notification_repository import NotificationRepository
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError


class CreateRequestDTO(TypedDict):
    title: str
    state: bool
    user_id: int
    description: str


class NotificationService:
    def __init__(self, notification_repository: NotificationRepository) -> None:
        self.__notification_repository = notification_repository

    def create(self, data: CreateRequestDTO):
        try:
            return self.__notification_repository.create(data)
        except IntegrityError:
            raise HTTPException(
                status_code=500,
                detail="Error creating notification",
            )

    def get_all(self, user_id: int):
        return self.__notification_repository.get_all_by_user_id(user_id)

    def mark_as_read(self, id: int):
        try:
            self.__notification_repository.mark_as_read(id)
        except Exception as e:
            raise e
