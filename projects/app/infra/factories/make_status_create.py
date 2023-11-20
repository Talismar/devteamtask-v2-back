from fastapi import Depends

from app.application.use_cases import StatusCreateUseCase
from app.infra.repositories import (
    ProjectSqlalchemyRepository,
    StatusSqlalchemyRepository,
)

from ..dependencies import database_connection


def make_status_create(session=Depends(database_connection)):
    status_repository = StatusSqlalchemyRepository(session)
    project_repository = ProjectSqlalchemyRepository(session)
    use_case = StatusCreateUseCase(status_repository, project_repository)
    return use_case
