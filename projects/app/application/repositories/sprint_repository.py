from abc import ABC, abstractmethod

from app.application.dtos import SprintPartialUpdateRequestDTO
from app.domain.entities.sprint import Sprint


class SprintRepository(ABC):
    @abstractmethod
    def create(self, data: Sprint) -> Sprint:
        pass

    @abstractmethod
    def partial_update(self, id: int, data: SprintPartialUpdateRequestDTO):
        pass

    # @abstractmethod
    # def delete(self, id: int):
    #     pass
