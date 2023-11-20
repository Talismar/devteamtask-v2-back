from uuid import UUID

from app.application.repositories import ProjectRepository


class ProjectAddCollaboratorUseCase:
    def __init__(self, project_repository: ProjectRepository) -> None:
        self.__project_repository = project_repository

    def execute(self, project_id: UUID, user_id: int):
        try:
            return self.__project_repository.add_collaborator(project_id, user_id)
        except Exception as e:
            raise e
