from fastapi import Depends

from app.application.use_cases import DailyCreateUseCase
from app.infra.repositories import DailySqlalchemyRepository

from ..dependencies import database_connection


def make_daily_create(session=Depends(database_connection)):
    repository = DailySqlalchemyRepository(session)
    use_case = DailyCreateUseCase(repository)
    return use_case
