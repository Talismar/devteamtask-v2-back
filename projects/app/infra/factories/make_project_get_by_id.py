from app.application.use_cases import ProjectGetByIdUseCase
from app.infra.repositories import ProjectSqlalchemyRepository
from app.infra.utils import FileStorageUtils
from app.main.configuration.local import settings
from fastapi import Depends

BASE_URL = f"{settings.BASE_URL}api/project/"

from ..dependencies import database_connection


def make_project_get_by_id(session=Depends(database_connection)):
    repository = ProjectSqlalchemyRepository(session)
    file_storage_utils = FileStorageUtils(["media", "project", "images"], BASE_URL)
    use_case = ProjectGetByIdUseCase(repository, file_storage_utils)
    return use_case
