from app.application.repositories import StatusRepository
from app.domain.errors import ResourceNotFoundException


class StatusGetByIdUseCase:
    def __init__(self, status_repository: StatusRepository) -> None:
        self.__status_repository = status_repository

    def execute(self, id: int):
        data = self.__status_repository.get_by_id(id)

        if data is None:
            raise ResourceNotFoundException("Status")

        return data
