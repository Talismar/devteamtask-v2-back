from uuid import UUID

from app.application.repositories import ProjectRepository
from app.domain.errors import ResourceNotFoundException


class ProjectDeleteUseCase:
    def __init__(self, project_repository: ProjectRepository) -> None:
        self.__project_repository = project_repository

    def execute(self, id: UUID):
        try:
            return self.__project_repository.delete(id)
        except ResourceNotFoundException as e:
            raise e
