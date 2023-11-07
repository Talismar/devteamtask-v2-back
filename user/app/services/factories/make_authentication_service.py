from fastapi import Depends
from ..authentication import AuthenticationService
from app.repositories.sqlalchemy.sqlalchemy_user_repository import (
    SqlalchemyUserRepository,
)
from app.dependencies import get_db_connection


def make_authentication_service(session=Depends(get_db_connection)):
    user_repository = SqlalchemyUserRepository(session)
    return AuthenticationService(user_repository)
