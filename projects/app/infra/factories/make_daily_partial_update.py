from fastapi import Depends

from app.application.use_cases import DailyPartialUpdateUseCase
from app.infra.repositories import DailySqlalchemyRepository

from ..dependencies import database_connection


def make_daily_partial_update(session=Depends(database_connection)):
    repository = DailySqlalchemyRepository(session)
    use_case = DailyPartialUpdateUseCase(repository)
    return use_case
