from app.application.use_cases import ProjectRemoveTagStatusUseCase
from app.infra.repositories import (
    ProjectSqlalchemyRepository,
    StatusSqlalchemyRepository,
    TagSqlalchemyRepository,
)
from fastapi import Depends

from ..dependencies import database_connection


def make_project_remove_tag_status(session=Depends(database_connection)):
    project_repository = ProjectSqlalchemyRepository(session)
    tag_repository = TagSqlalchemyRepository(session)
    status_repository = StatusSqlalchemyRepository(session)

    use_case = ProjectRemoveTagStatusUseCase(
        project_repository, status_repository, tag_repository
    )
    return use_case
