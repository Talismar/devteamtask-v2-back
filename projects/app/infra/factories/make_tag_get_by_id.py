from app.application.use_cases import TagGetByIdUseCase
from app.infra.repositories import TagSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_tag_get_by_id(session=Depends(database_connection)):
    repository = TagSqlalchemyRepository(session)
    use_case = TagGetByIdUseCase(repository)
    return use_case
