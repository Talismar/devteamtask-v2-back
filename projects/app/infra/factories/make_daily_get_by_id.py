from fastapi import Depends

from app.application.use_cases import DailyGetByIdUseCase
from app.infra.repositories import DailySqlalchemyRepository

from ..dependencies import database_connection


def make_daily_get_by_id(session=Depends(database_connection)):
    repository = DailySqlalchemyRepository(session)
    use_case = DailyGetByIdUseCase(repository)
    return use_case
