from app.application.use_cases import SprintCreateUseCase
from app.infra.repositories import (
    ProjectSqlalchemyRepository,
    SprintSqlalchemyRepository,
)
from fastapi import Depends

from ..dependencies import database_connection


def make_sprint_create(session=Depends(database_connection)):
    sprint_repository = SprintSqlalchemyRepository(session)
    project_repository = ProjectSqlalchemyRepository(session)
    use_case = SprintCreateUseCase(sprint_repository, project_repository)
    return use_case
