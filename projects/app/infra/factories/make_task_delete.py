from app.application.use_cases import TaskDeleteUseCase
from app.infra.repositories import TaskSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_task_delete(session=Depends(database_connection)):
    repository = TaskSqlalchemyRepository(session)
    use_case = TaskDeleteUseCase(repository)
    return use_case
