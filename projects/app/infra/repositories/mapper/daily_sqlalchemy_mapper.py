from app.domain.entities.daily import Daily
from app.infra.database.models import DailyModel


class DailySqlalchemyMapper:
    @staticmethod
    def toDomain(raw: DailyModel) -> Daily:
        return {
            "id": raw.id,
            "note": raw.note,
            "event_notes_id": raw.event_notes_id,
            "created_at": raw.created_at,
            "updated_at": raw.updated_at,
        }
