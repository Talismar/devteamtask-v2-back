from app.application.repositories import EventNotesRepository
from app.domain.entities.event_notes import EventNotes


class EventNotesPartialUpdateUseCase:
    def __init__(self, event_notes_repository: EventNotesRepository) -> None:
        self.__event_notes_repository = event_notes_repository

    def execute(self, id: int, data: EventNotes):
        return self.__event_notes_repository.partial_update(id, data)
