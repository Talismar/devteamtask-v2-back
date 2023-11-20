from app.domain.entities.user import User
from app.infra.database import UserModel


class UserSqlalchemyMapper:
    @staticmethod
    def toDomain(raw: UserModel) -> User:
        # result = {}

        # for column in raw.__table__.columns:
        #     result[column.name] = getattr(raw, column.name)

        return {
            "id": raw.id,
            "name": raw.name,
            "email": raw.email,
            "password": raw.password,
            "avatar_url": raw.avatar_url,
            "auth_provider": raw.auth_provider,
            "created_at": raw.created_at,
            "updated_at": raw.updated_at,
            "notification_state": raw.notification_state,
            "notifications": raw.notifications,
        }

    @staticmethod
    def toSqlAlchemy(data: User):
        return UserModel(**data)
