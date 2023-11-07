from app.application.use_cases import ProjectGetAllUseCase
from app.infra.repositories import ProjectSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_project_get_all(session=Depends(database_connection)):
    repository = ProjectSqlalchemyRepository(session)
    use_case = ProjectGetAllUseCase(repository)
    return use_case
