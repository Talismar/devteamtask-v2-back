from app.application.repositories import TaskRepository
from app.domain.errors import ResourceNotFoundException
from app.domain.feedback import SuccessFulCreationFeedback


class TaskDeleteUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.__task_repository = task_repository

    def execute(self, id: int):
        was_deleted = self.__task_repository.delete(id)

        if not was_deleted:
            raise ResourceNotFoundException("Task")
