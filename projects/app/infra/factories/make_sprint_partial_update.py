from fastapi import Depends

from app.application.use_cases import SprintPartialUpdateUseCase
from app.infra.repositories import SprintSqlalchemyRepository

from ..dependencies import database_connection


def make_sprint_partial_update(session=Depends(database_connection)):
    sprint_repository = SprintSqlalchemyRepository(session)
    use_case = SprintPartialUpdateUseCase(sprint_repository)
    return use_case
