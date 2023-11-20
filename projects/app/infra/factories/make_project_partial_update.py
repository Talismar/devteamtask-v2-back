from time import sleep

from fastapi import Depends

from app.application.use_cases import ProjectPartialUpdateUseCase
from app.infra.repositories import ProjectSqlalchemyRepository
from app.infra.utils import FileStorageUtils, SendEmailService
from app.main.configuration.local import settings

from ..dependencies import database_connection

BASE_URL = str(settings.BASE_URL).replace("localhost", "127.0.0.1")
BASE_URL = f"{BASE_URL}api/project/"


def make_project_partial_update(session=Depends(database_connection)):
    send_email_service = SendEmailService("Project")
    repository = ProjectSqlalchemyRepository(session)
    file_storage_utils = FileStorageUtils(["media", "project", "images"], BASE_URL)
    use_case = ProjectPartialUpdateUseCase(
        repository, file_storage_utils, send_email_service
    )
    return use_case
