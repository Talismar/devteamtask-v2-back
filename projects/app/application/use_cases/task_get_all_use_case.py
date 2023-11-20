from app.application.repositories import TaskRepository


class TaskGetAllUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def execute(self):
        return self.task_repository.get_all()
