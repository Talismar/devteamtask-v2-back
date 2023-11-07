from app.application.use_cases import TaskPartialUpdateUseCase
from app.infra.repositories import TaskSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_task_partial_update(session=Depends(database_connection)):
    repository = TaskSqlalchemyRepository(session)
    use_case = TaskPartialUpdateUseCase(repository)
    return use_case
