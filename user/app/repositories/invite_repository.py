from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar
from uuid import UUID

T = TypeVar("T")
TMODEL = TypeVar("TMODEL")


class InviteRepository(ABC, Generic[T, TMODEL]):
    def __init__(self, db: T) -> None:
        self._db = db

    @abstractmethod
    def create(self, data: Any) -> TMODEL:
        pass

    @abstractmethod
    def get_by_token(self, token: UUID) -> TMODEL:
        pass

    def save(self) -> TMODEL:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
