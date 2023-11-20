from app.application.dtos import SprintPartialUpdateRequestDTO
from app.application.repositories import SprintRepository


class SprintPartialUpdateUseCase:
    def __init__(self, sprint_repository: SprintRepository) -> None:
        self.__sprint_repository = sprint_repository

    def execute(self, id: int, data: SprintPartialUpdateRequestDTO):
        return self.__sprint_repository.partial_update(id, data)
