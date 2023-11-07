from fastapi import Depends
from ..user import UserService
from app.repositories.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository,
)
from app.dependencies import get_db_connection


def make_user_service(session=Depends(get_db_connection)):
    user_repository = SqlalchemyUserRepository(session)
    return UserService(user_repository)
