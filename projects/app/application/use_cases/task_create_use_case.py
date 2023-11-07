from ..interfaces.repositories import TaskRepository


class TaskCreateUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.__task_repository = task_repository

    def execute(self, data: dict):
        try:
            return self.__task_repository.create(data)
        except Exception as e:
            raise e
