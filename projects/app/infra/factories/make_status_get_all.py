from app.application.use_cases import StatusGetAllUseCase
from app.infra.repositories import StatusSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_status_get_all(session=Depends(database_connection)):
    repository = StatusSqlalchemyRepository(session)
    use_case = StatusGetAllUseCase(repository)
    return use_case
