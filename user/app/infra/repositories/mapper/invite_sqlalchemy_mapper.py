from app.domain.entities.invite import Invite
from app.infra.database import InviteModel


class InviteSqlalchemyMapper:
    @staticmethod
    def toDomain(raw: InviteModel) -> Invite:
        return {
            "id": raw.id,
            "token": raw.token,
            "resource_id": raw.resource_id,
            "email": raw.email,
            "resource_name": raw.resource_name,
            "expiration_date": raw.expiration_date,
            "created_at": raw.created_at,
            "updated_at": raw.updated_at,
        }
