from app.application.use_cases import TaskGetByIdUseCase
from app.infra.repositories import TaskSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_task_get_by_id(session=Depends(database_connection)):
    repository = TaskSqlalchemyRepository(session)
    use_case = TaskGetByIdUseCase(repository)
    return use_case
