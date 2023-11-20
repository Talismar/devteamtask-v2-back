from fastapi import Depends

from app.application.use_cases import EventNotesPartialUpdateUseCase
from app.infra.repositories import EventNotesSqlalchemyRepository

from ..dependencies import database_connection


def make_event_notes_partial_update(session=Depends(database_connection)):
    repository = EventNotesSqlalchemyRepository(session)
    use_case = EventNotesPartialUpdateUseCase(repository)
    return use_case
