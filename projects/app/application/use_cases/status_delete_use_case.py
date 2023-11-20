from app.application.repositories import StatusRepository
from app.domain.errors import ResourceNotFoundException
from app.domain.feedback import SuccessFulCreationFeedback


class StatusDeleteUseCase:
    def __init__(self, status_repository: StatusRepository) -> None:
        self.__status_repository = status_repository

    def execute(self, id: int):
        was_deleted = self.__status_repository.delete(id)

        if not was_deleted:
            raise ResourceNotFoundException("Status")

        return SuccessFulCreationFeedback("Status", " deleted successfully").message
