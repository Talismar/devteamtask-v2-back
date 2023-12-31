import re
from uuid import UUID

from app.application.repositories import TaskRepository
from app.domain.errors import ResourceNotFoundException


class WebhookTaskUpdateStatusUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.__task_repository = task_repository

    def get_task_id_by_commit_message(self, commit_message: str):
        match = re.search(r"DDT-(\d+):", commit_message)

        if match:
            return match.group(1)

    def execute(self, commit_message: str, project_id: UUID):
        task_id = self.get_task_id_by_commit_message(commit_message)

        if isinstance(task_id, str) and task_id.isnumeric():
            task_id = int(task_id)
            try:
                return self.__task_repository.update_status_by_id_and_project_id(
                    task_id, project_id, "Done"
                )
            except ResourceNotFoundException as e:
                raise e
