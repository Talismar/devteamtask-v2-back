from app.application.use_cases import ProjectPartialUpdateUseCase
from app.infra.repositories import ProjectSqlalchemyRepository
from app.infra.utils import FileStorageUtils, SendEmailService
from app.main.configuration.local import settings
from fastapi import Depends

from ..dependencies import database_connection

BASE_URL = f"{settings.BASE_URL}api/project/"


def make_project_partial_update(session=Depends(database_connection)):
    send_email_service = SendEmailService("Project")
    repository = ProjectSqlalchemyRepository(session)
    file_storage_utils = FileStorageUtils(["media", "project", "images"], BASE_URL)
    use_case = ProjectPartialUpdateUseCase(
        repository, file_storage_utils, send_email_service
    )
    return use_case
