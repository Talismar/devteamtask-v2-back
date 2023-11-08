from uuid import UUID

from app.domain.errors import ResourceNotFoundException

from ..interfaces.repositories import ProjectRepository, StatusRepository


class ProjectDeleteUseCase:
    def __init__(self, project_repository: ProjectRepository) -> None:
        self.__project_repository = project_repository

    def execute(self, id: UUID):
        try:
            return self.__project_repository.delete(id)
        except ResourceNotFoundException as e:
            raise e
