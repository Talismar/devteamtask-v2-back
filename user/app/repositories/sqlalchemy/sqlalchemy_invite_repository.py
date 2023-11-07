from app.models import InviteModel
from app.repositories.invite_repository import InviteRepository
from app.schemas.user import UserPostRequestSchema
from sqlalchemy.orm import Session


class SqlalchemyInviteRepository(InviteRepository[Session, InviteModel]):
    def create(self, data: dict):
        instance = InviteModel(**data)

        self._db.add(instance)
        self._db.commit()
        self._db.refresh(instance)

        return instance

    def get_by_token(self, token):
        return self._db.query(InviteModel).filter_by(token=token).first()

    def delete(self, id):
        obj = self._db.get(InviteModel, id)
        self._db.delete(obj)
        self._db.commit()
