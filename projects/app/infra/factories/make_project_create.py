from app.application.use_cases import ProjectCreateUseCase
from app.infra.repositories import (
    ProjectSqlalchemyRepository,
    StatusSqlalchemyRepository,
)
from fastapi import Depends

from ..dependencies import database_connection


def make_project_create(session=Depends(database_connection)):
    project_repository = ProjectSqlalchemyRepository(session)
    status_repository = StatusSqlalchemyRepository(session)
    use_case = ProjectCreateUseCase(project_repository, status_repository)
    return use_case
