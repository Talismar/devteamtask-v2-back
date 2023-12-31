from uuid import UUID

from app.application.repositories import TaskRepository


class TaskGetAllUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def execute(self, project_id: UUID, task_name: None | str):
        return self.task_repository.get_all_by_project_id(project_id, task_name)
