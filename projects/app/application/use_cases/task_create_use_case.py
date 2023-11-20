from app.application.dtos import TaskCreateRequestDTO
from app.application.repositories import TaskRepository


class TaskCreateUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.__task_repository = task_repository

    def execute(self, data: TaskCreateRequestDTO):
        try:
            tags_ids = data.pop("tags_ids", [])

            task = self.__task_repository.create(data, tags_ids)

            return task
        except Exception as e:
            raise e
