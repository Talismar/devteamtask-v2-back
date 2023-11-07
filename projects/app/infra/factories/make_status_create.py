from app.application.use_cases import StatusCreateUseCase
from app.infra.repositories import StatusSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_status_create(session=Depends(database_connection)):
    repository = StatusSqlalchemyRepository(session)
    use_case = StatusCreateUseCase(repository)
    return use_case
