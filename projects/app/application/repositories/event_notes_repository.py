from abc import ABC, abstractmethod

from app.domain.entities.event_notes import EventNotes


class EventNotesRepository(ABC):
    @abstractmethod
    def create(self, data: EventNotes) -> EventNotes:
        pass

    @abstractmethod
    def partial_update(self, id: int, data: EventNotes):
        pass

    @abstractmethod
    def get_by_sprint_id(self, sprint_id: int) -> EventNotes:
        pass

    # @abstractmethod
    # def delete(self, id: int):
    #     pass
