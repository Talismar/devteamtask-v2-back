from app.application.use_cases import ProjectAddCollaboratorUseCase
from app.infra.repositories import (
    ProjectSqlalchemyRepository
)
from fastapi import Depends

from ..dependencies import database_connection


def make_project_add_collaborator(session=Depends(database_connection)):
    project_repository = ProjectSqlalchemyRepository(session)

    use_case = ProjectAddCollaboratorUseCase(
        project_repository
    )
    return use_case
