from uuid import UUID

from app.application.abstract_media_storages import AbstractMediaStorages
from app.application.repositories import ProjectRepository
from app.domain.errors import ResourceNotFoundException


class ProjectGetByIdUseCase:
    def __init__(
        self,
        project_repository: ProjectRepository,
        media_storages: AbstractMediaStorages,
    ) -> None:
        self.__project_repository = project_repository
        self.media_storages = media_storages

    def execute(self, id: UUID):
        project = self.__project_repository.get_by_id(id)

        if project is None:
            raise ResourceNotFoundException("Project")

        users = []
        users_ids: set[int] = set()

        if project["product_owner_id"] is not None:
            users_ids.add(project["product_owner_id"])

        if len(project["collaborators_ids"]) > 0:
            users_ids.update(project["collaborators_ids"])

        if len(project["sprints"]) > 0:
            project["current_sprint"] = project["sprints"][0]
        else:
            project["current_sprint"] = None

        if len(users_ids) > 0:
            users = self.__project_repository.get_users_data(tuple(users_ids))  # type: ignore

        if isinstance(project["logo_url"], str):
            project["logo_url"] = self.media_storages.get_url_media(project["logo_url"])

        return {
            "project_data": project,
            "users": users,
        }
