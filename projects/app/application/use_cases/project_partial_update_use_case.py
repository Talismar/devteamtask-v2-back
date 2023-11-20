from uuid import UUID

from app.application.abstract_email_service import AbstractEmailService
from app.application.abstract_media_storages import AbstractMediaStorages
from app.application.dtos import ProjectPartialUpdateRequestDTO
from app.application.repositories import ProjectRepository
from app.domain.errors import ResourceNotFoundException


class ProjectPartialUpdateUseCase:
    def __init__(
        self,
        project_repository: ProjectRepository,
        media_storages: AbstractMediaStorages,
        email_service: AbstractEmailService,
    ):
        self.__project_repository = project_repository
        self.media_storages = media_storages
        self.email_service = email_service

    def execute(self, id: UUID, data_to_update: ProjectPartialUpdateRequestDTO):
        project = self.__project_repository.get_by_id(id)

        if project is None:
            raise ResourceNotFoundException("Project")

        logo_url = data_to_update.pop("logo_url", None)
        product_owner_email = data_to_update.pop("product_owner_email", None)
        collaborator_emails = data_to_update.pop("collaborator_emails", None)

        if logo_url is not None:
            data_to_update["logo_url"] = self.media_storages.save_file(
                logo_url, project["logo_url"]
            )

        if product_owner_email is not None:
            try:
                self.email_service.send(
                    [product_owner_email],
                    str(project["id"]),
                    "add_product_owner",
                )
            except Exception as e:
                raise e

        if collaborator_emails is not None:
            try:
                self.email_service.send(
                    collaborator_emails,
                    str(project["id"]),
                    "add_collaborator",
                )
            except Exception as e:
                raise e

        if len(data_to_update) > 0:
            project_model_updated = self.__project_repository.partial_update(
                id, data_to_update
            )

            if (
                project_model_updated is not None
                and project_model_updated["logo_url"] is not None
            ):
                project_model_updated["logo_url"] = self.media_storages.get_url_media(
                    project_model_updated["logo_url"]
                )

            return {"project_data": project_model_updated, "users": []}

        return {"project_data": project, "users": []}
