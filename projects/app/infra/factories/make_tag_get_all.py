from app.application.use_cases import TagGetAllUseCase
from app.infra.repositories import TagSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_tag_get_all(session=Depends(database_connection)):
    repository = TagSqlalchemyRepository(session)
    use_case = TagGetAllUseCase(repository)
    return use_case
