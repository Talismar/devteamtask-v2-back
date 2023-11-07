from app.domain.errors import ResourceNotFoundException
from app.domain.feedback import SuccessFulCreationFeedback

from ..interfaces.repositories import StatusRepository


class StatusDeleteUseCase:
    def __init__(self, status_repository: StatusRepository) -> None:
        self.__status_repository = status_repository

    def execute(self, id: int):
        was_deleted = self.__status_repository.delete(id)

        if not was_deleted:
            raise ResourceNotFoundException("Status")

        return SuccessFulCreationFeedback("Status").message
