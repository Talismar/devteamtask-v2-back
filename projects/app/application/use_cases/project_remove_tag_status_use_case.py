from uuid import UUID

from app.application.repositories import (
    ProjectRepository,
    StatusRepository,
    TagRepository,
)
from app.domain.errors import ResourceNotFoundException


class ProjectRemoveTagStatusUseCase:
    def __init__(
        self,
        project_repository: ProjectRepository,
        status_repository: StatusRepository,
        tag_repository: TagRepository,
    ) -> None:
        self.__project_repository = project_repository
        self.__status_repository = status_repository
        self.__tag_repository = tag_repository

    def execute(self, project_id: UUID, resource_name: str, resource_id: int):
        project_instance = self.__project_repository.get_by_id(project_id)

        if project_instance is None:
            raise ResourceNotFoundException("Project")

        if resource_name == "Tag":
            tags_ids = [tag.id for tag in project_instance.tags]

            if resource_id in tags_ids:
                tag_instance = self.__tag_repository.get_by_id(resource_id)

                if tag_instance is None:
                    raise ResourceNotFoundException("Tag")

                project_instance.tags.remove(tag_instance)
                project_instance = self.__project_repository.save(project_instance)
            else:
                raise ResourceNotFoundException("Tag")

        elif resource_name == "Status":
            status_ids = [status.id for status in project_instance.status]

            if resource_id in status_ids:
                status_instance = self.__status_repository.get_by_id(resource_id)

                if status_instance is None:
                    raise ResourceNotFoundException("Status")

                project_instance.status.remove(status_instance)
                project_instance = self.__project_repository.save(project_instance)
            else:
                raise ResourceNotFoundException("Status")

        return project_instance
