from abc import ABC
from datetime import datetime
from typing import BinaryIO, TypedDict

from app.domain.errors import ResourceNotFoundException
from app.domain.feedback import SuccessFulCreationFeedback

from ..interfaces.repositories import ProjectRepository


class FileTypes(TypedDict):
    file: BinaryIO
    filename: None | str


class FileStorageUtils:
    def __init__(self, relative_path: list[str], base_url: str) -> None:
        self.relative_path = relative_path
        self.base_url = base_url

    def save_file(self, new_file: any, original_filename: str | None = None):
        pass

    def get_url_media(self, filename: str):
        pass


class ProjectPartialUpdateDTO(TypedDict):
    name: None | str
    state: None | str
    logo_url: None | FileTypes
    end_date: None | datetime
    product_owner_email: None | str


class SendEmailService(ABC):
    def send(self, email: str, resource_id: int):
        pass


class ProjectPartialUpdateUseCase:
    def __init__(
        self,
        project_repository: ProjectRepository,
        file_storage_utils: FileStorageUtils,
        send_email_service: SendEmailService,
    ) -> None:
        self.__project_repository = project_repository
        self.file_storage_utils = file_storage_utils
        self.send_email_service = send_email_service

    def execute(self, id: int, data_to_update: ProjectPartialUpdateDTO):
        project_model = self.__project_repository.get_by_id(id)

        if project_model is None:
            raise ResourceNotFoundException("Project")

        logo_url = data_to_update.pop("logo_url", None)
        product_owner_email = data_to_update.pop("product_owner_email", None)

        if logo_url is not None:
            project_model.logo_url = self.file_storage_utils.save_file(
                logo_url, project_model.logo_url
            )

        if product_owner_email is not None:
            self.send_email_service.send([product_owner_email], project_model.id)

        project_model_updated = self.__project_repository.partial_update(
            project_model, data_to_update
        )

        project_model_updated.logo_url = self.file_storage_utils.get_url_media(
            project_model_updated.logo_url
        )

        return project_model_updated
