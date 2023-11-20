from abc import ABC, abstractmethod

from app.domain.entities.daily import Daily


class DailyRepository(ABC):
    @abstractmethod
    def create(self, sprint_id: int, data: Daily) -> Daily:
        pass

    @abstractmethod
    def partial_update(self, id: int, data: Daily):
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Daily:
        pass

    @abstractmethod
    def get_all_by_sprint_id(self, sprint_id: int) -> list[Daily]:
        pass
