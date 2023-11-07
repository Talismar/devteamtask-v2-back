from app.application.use_cases import TagCreateUseCase
from app.infra.repositories import ProjectSqlalchemyRepository, TagSqlalchemyRepository
from fastapi import Depends

from ..dependencies import database_connection


def make_tag_create(session=Depends(database_connection)):
    project_repository = ProjectSqlalchemyRepository(session)
    tag_repository = TagSqlalchemyRepository(session)

    use_case = TagCreateUseCase(tag_repository, project_repository)
    return use_case
