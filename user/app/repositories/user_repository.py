from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from app.schemas.user import UserSchema

from ..models.user import UserModel

T = TypeVar("T")


class UserRepository(ABC, Generic[T]):
    def __init__(self, db: T) -> None:
        self._db = db

    @abstractmethod
    def list_all(self) -> list[UserSchema]:
        pass

    @abstractmethod
    def create(self, user: Any) -> UserModel:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> UserModel:
        pass

    @abstractmethod
    def get_by_email(self, user_id: str) -> UserModel | None:
        pass

    @abstractmethod
    def partial_update(
        self, user_id: int, task_instance, data_to_update: dict
    ) -> UserModel:
        pass

    def save(self):
        self._db.commit()

    @abstractmethod
    def delete(self, id: int):
        ...
