from app.application.use_cases import StatusGetByIdUseCase
from app.infra.repositories import StatusSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_status_get_by_id(session=Depends(database_connection)):
    repository = StatusSqlalchemyRepository(session)
    use_case = StatusGetByIdUseCase(repository)
    return use_case
