from fastapi import Depends

from app.application.use_cases import ProjectGetByIdUseCase
from app.infra.dependencies import database_connection
from app.infra.repositories import ProjectSqlalchemyRepository
from app.infra.utils import FileStorageUtils
from app.main.configuration.local import settings

BASE_URL = str(settings.BASE_URL).replace("localhost", "127.0.0.1")
BASE_URL = f"{BASE_URL}api/project/"


def make_project_get_by_id(session=Depends(database_connection)):
    repository = ProjectSqlalchemyRepository(session)
    file_storage_utils = FileStorageUtils(["media", "project", "images"], BASE_URL)
    use_case = ProjectGetByIdUseCase(repository, file_storage_utils)
    return use_case
