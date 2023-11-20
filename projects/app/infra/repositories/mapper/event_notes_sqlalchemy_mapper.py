from app.domain.entities.event_notes import EventNotes
from app.infra.database.models import EventNotesModel


class EventNotesSqlalchemyMapper:
    @staticmethod
    def toDomain(raw: EventNotesModel) -> EventNotes:
        return {
            "id": raw.id,
            "planning": raw.planning,
            "retrospective": raw.retrospective,
            "review": raw.review,
            "sprint_id": raw.sprint_id,
        }
