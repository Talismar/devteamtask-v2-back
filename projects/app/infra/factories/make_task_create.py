from app.application.use_cases import TaskCreateUseCase
from app.infra.repositories import TaskSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_task_create(session=Depends(database_connection)):
    repository = TaskSqlalchemyRepository(session)
    use_case = TaskCreateUseCase(repository)
    return use_case
