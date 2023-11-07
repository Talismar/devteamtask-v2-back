from app.application.use_cases import TaskDashboardDataUseCase
from app.infra.repositories import TaskSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_task_dashboard_data(session=Depends(database_connection)):
    repository = TaskSqlalchemyRepository(session)
    use_case = TaskDashboardDataUseCase(repository)
    return use_case
