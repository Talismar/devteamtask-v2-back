from app.application.use_cases import ProjectDeleteUseCase
from app.infra.repositories import ProjectSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_project_delete(session=Depends(database_connection)):
    repository = ProjectSqlalchemyRepository(session)
    use_case = ProjectDeleteUseCase(repository)
    return use_case
