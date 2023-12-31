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
        self.project_repository = project_repository
        self.status_repository = status_repository
        self.tag_repository = tag_repository

    def execute(self, project_id: UUID, resource_name: str, resource_id: int):
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ResourceNotFoundException("Project")

        if resource_name == "Tag":
            tags_ids = [tag["id"] for tag in project["tags"]]

            if resource_id in tags_ids:
                tag_instance = self.tag_repository.get_by_id(resource_id)

                project = self.project_repository.remove_tag(
                    project["id"], tag_instance
                )
            else:
                raise ResourceNotFoundException("Tag")

        elif resource_name == "Status":
            status_ids = [status["id"] for status in project["status"]]

            if resource_id in status_ids:
                status_instance = self.status_repository.get_by_id(resource_id)

                project = self.project_repository.remove_status(
                    project["id"], status_instance
                )
            else:
                raise ResourceNotFoundException("Status")

        return project
