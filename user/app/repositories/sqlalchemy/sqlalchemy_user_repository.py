from app.models import UserModel
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserPostRequestSchema
from sqlalchemy.orm import Session


class SqlalchemyUserRepository(UserRepository[Session]):
    def list_all(self):
        return self._db.query(UserModel).all()

    def create(self, user: UserPostRequestSchema):
        db_user = UserModel(**user.model_dump())

        self._db.add(db_user)
        self._db.commit()
        self._db.refresh(db_user)

        return db_user

    def get_by_id(self, id: int):
        return self._db.query(UserModel).filter_by(id=id).first()

    def get_by_email(self, email: str):
        return self._db.query(UserModel).filter_by(email=email).first()

    def partial_update(self, id: int, instance: UserModel, data_to_update: dict):
        for field, value in data_to_update.items():
            if value is not None:
                setattr(instance, field, value)

        self._db.commit()
        return instance

    def delete(self, id):
        obj = self._db.get(UserModel, id)
        self._db.delete(obj)
        self._db.commit()
