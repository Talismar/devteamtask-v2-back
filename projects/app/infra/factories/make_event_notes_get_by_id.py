from fastapi import Depends

from app.application.use_cases import EventNotesGetByIdUseCase
from app.infra.repositories import EventNotesSqlalchemyRepository

from ..dependencies import database_connection


def make_event_notes_get_by_id(session=Depends(database_connection)):
    repository = EventNotesSqlalchemyRepository(session)
    use_case = EventNotesGetByIdUseCase(repository)
    return use_case
