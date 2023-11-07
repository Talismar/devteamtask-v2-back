from app.application.use_cases import StatusDeleteUseCase
from app.infra.repositories import StatusSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_status_delete(session=Depends(database_connection)):
    repository = StatusSqlalchemyRepository(session)
    use_case = StatusDeleteUseCase(repository)
    return use_case
