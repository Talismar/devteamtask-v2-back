from sqlalchemy import update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.application.repositories import UserRepository
from app.domain.entities.user import User
from app.domain.errors import DatabaseException, ResourceNotFoundException
from app.infra.database.models import UserModel

from .mapper.user_sqlalchemy_mapper import UserSqlalchemyMapper


class UserSqlalchemyRepository(UserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def list_all(self):
        user_models = self.session.query(UserModel).all()
        return [UserSqlalchemyMapper.toDomain(row) for row in user_models]

    def create(self, data):
        user_model = UserSqlalchemyMapper.toSqlAlchemy(data)

        try:
            self.session.add(user_model)
            self.session.commit()
            self.session.refresh(user_model)
        except IntegrityError:
            raise DatabaseException("Account already exists", 409)

        return UserSqlalchemyMapper.toDomain(user_model)

    def get_by_id(self, id):
        user_model = self.session.query(UserModel).filter_by(id=id).first()

        if user_model is not None:
            return UserSqlalchemyMapper.toDomain(user_model)

        return None

    def get_by_email(self, email):
        user_model = self.session.query(UserModel).filter_by(email=email).first()

        if user_model is not None:
            return UserSqlalchemyMapper.toDomain(user_model)

        return None

    def partial_update(self, id, data_to_update):
        stmt = (
            update(UserModel)
            .where(UserModel.id == id)
            .values(**data_to_update)
            .returning(UserModel)
        )
        result = self.session.execute(stmt)
        updated_data = result.fetchone()
        self.session.commit()

        return UserSqlalchemyMapper.toDomain(updated_data[0])

    def delete(self, id):
        user_mode = self.session.get(UserModel, id)

        if user_mode is not None:
            raise ResourceNotFoundException("User")

        self.session.delete(user_mode)
        self.session.commit()
