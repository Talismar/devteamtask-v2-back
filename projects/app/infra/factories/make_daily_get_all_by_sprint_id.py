from fastapi import Depends

from app.application.use_cases import DailyGetAllBySprintIdUseCase
from app.infra.repositories import DailySqlalchemyRepository

from ..dependencies import database_connection


def make_daily_get_all_by_sprint_id(session=Depends(database_connection)):
    repository = DailySqlalchemyRepository(session)
    use_case = DailyGetAllBySprintIdUseCase(repository)
    return use_case
