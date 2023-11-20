from fastapi import Depends

from app.application.use_cases import SprintCreateUseCase
from app.infra.repositories import (
    EventNotesSqlalchemyRepository,
    ProjectSqlalchemyRepository,
    SprintSqlalchemyRepository,
)

from ..dependencies import database_connection


def make_sprint_create(session=Depends(database_connection)):
    sprint_repository = SprintSqlalchemyRepository(session)
    project_repository = ProjectSqlalchemyRepository(session)
    event_notes_repository = EventNotesSqlalchemyRepository(session)
    use_case = SprintCreateUseCase(
        sprint_repository, project_repository, event_notes_repository
    )
    return use_case
