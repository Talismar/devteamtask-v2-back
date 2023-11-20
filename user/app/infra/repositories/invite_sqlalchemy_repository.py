from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.application.repositories import InviteRepository
from app.domain.errors import DatabaseException
from app.infra.database import InviteModel

from .mapper.invite_sqlalchemy_mapper import InviteSqlalchemyMapper


class InviteSqlalchemyRepository(InviteRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, data):
        instance = InviteModel(**data)

        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)

        return InviteSqlalchemyMapper.toDomain(instance)

    def get_by_token(self, token):
        notification_model = (
            self.session.query(InviteModel).filter_by(token=token).first()
        )

        if notification_model is not None:
            return InviteSqlalchemyMapper.toDomain(notification_model)

        return None

    def delete(self, id):
        obj = self.session.get(InviteModel, id)
        self.session.delete(obj)
        self.session.commit()
