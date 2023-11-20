from app.domain.entities.status import Status
from app.infra.database.models import StatusModel


class StatusSqlalchemyMapper:
    @staticmethod
    def toDomain(raw: StatusModel) -> Status:
        return Status(raw.name, raw.id)
