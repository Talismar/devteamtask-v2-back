from app.application.use_cases import TaskGetAllUseCase
from app.infra.repositories import TaskSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_task_get_all(session=Depends(database_connection)):
    repository = TaskSqlalchemyRepository(session)
    use_case = TaskGetAllUseCase(repository)
    return use_case
