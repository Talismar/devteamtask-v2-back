from ..interfaces.repositories import TaskRepository


class TaskGetAllUseCase:
    def __init__(self, status_repository: TaskRepository) -> None:
        self.__status_repository = status_repository

    def execute(self):
        return self.__status_repository.get_all()
