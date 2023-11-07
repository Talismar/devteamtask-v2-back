from abc import ABC, abstractmethod
from typing import Generic, TypedDict, TypeVar

TSESSION = TypeVar("TSESSION")
TMODEL = TypeVar("TMODEL")


class CreateRequestDTO(TypedDict):
    title: str
    state: bool
    user_id: int
    description: str


class NotificationRepository(ABC, Generic[TSESSION, TMODEL]):
    def __init__(self, session: TSESSION) -> None:
        self._session = session

    @abstractmethod
    def create(self, data: CreateRequestDTO) -> TMODEL:
        pass

    @abstractmethod
    def mark_as_read(self, id: int) -> TMODEL:
        pass

    @abstractmethod
    def get_all_by_user_id(self, user_id: int) -> list[TMODEL]:
        pass
