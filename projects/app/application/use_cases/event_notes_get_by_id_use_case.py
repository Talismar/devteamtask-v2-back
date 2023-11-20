from app.application.repositories import EventNotesRepository


class EventNotesGetByIdUseCase:
    def __init__(self, event_notes_repository: EventNotesRepository) -> None:
        self.__event_notes_repository = event_notes_repository

    def execute(self, sprint_id: int):
        return self.__event_notes_repository.get_by_sprint_id(sprint_id)
