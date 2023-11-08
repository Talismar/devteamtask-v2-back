from app.domain.errors import ResourceNotFoundException
from app.domain.feedback import SuccessFulCreationFeedback

from ..interfaces.repositories import TaskRepository


class TaskPartialUpdateUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.__task_repository = task_repository

    def execute(self, id: int, data):
        try:
            return self.__task_repository.partial_update(id, data)
        except ResourceNotFoundException as e:
            raise e
