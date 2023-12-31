from abc import ABC, abstractmethod
from datetime import date as datetime_date
from typing import TypedDict
from uuid import UUID

from app.domain.entities.task import Task


class CompletedInLastSevenDaysTypes(TypedDict):
    date: datetime_date
    amount: int


class TaskRepository(ABC):
    @abstractmethod
    def create(self, data: dict, tags_ids: list[int]) -> Task:
        pass

    @abstractmethod
    def get_all_by_project_id(self, project_id: UUID, task_name: None | str):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def partial_update(self, id: int, data):
        pass

    @abstractmethod
    def update_status_by_id_and_project_id(
        self, task_id: int, project_id: UUID, status: str
    ):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get_total_completed(self, user_id: int) -> int:
        pass

    @abstractmethod
    def get_total_assigned(self, user_id: int) -> int:
        pass

    @abstractmethod
    def get_total_completed_in_last_7_days(
        self, user_id: int
    ) -> list[CompletedInLastSevenDaysTypes]:
        pass

    @abstractmethod
    def get_total_pending_in_last_7_days(self, user_id: int) -> int:
        pass

    @abstractmethod
    def get_total_task_in_last_7_days(self, user_id: int) -> int:
        pass

    @abstractmethod
    def get_total_scheduled(self, user_id: int) -> int:
        pass
