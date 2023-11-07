from uuid import UUID

from app.domain.errors import ResourceNotFoundException

from ..interfaces.repositories import ProjectRepository
from .project_partial_update_use_case import FileStorageUtils


class ProjectGetByIdUseCase:
    def __init__(
        self,
        project_repository: ProjectRepository,
        file_storage_utils: FileStorageUtils,
    ) -> None:
        self.__project_repository = project_repository
        self.file_storage_utils = file_storage_utils

    def execute(self, id: UUID):
        instance = self.__project_repository.get_by_id(id)

        if instance is None:
            raise ResourceNotFoundException("Project")

        if isinstance(instance["project_data"]["logo_url"], str):
            instance["project_data"][
                "logo_url"
            ] = self.file_storage_utils.get_url_media(
                instance["project_data"]["logo_url"]
            )

        return instance
