from app.domain.errors import ResourceNotFoundException

from ..interfaces.repositories import TaskRepository


class TaskGetByIdUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.__task_repository = task_repository

    def execute(self, id: int):
        data = self.__task_repository.get_by_id(id)

        if data is None:
            raise ResourceNotFoundException("Task")

        return data
