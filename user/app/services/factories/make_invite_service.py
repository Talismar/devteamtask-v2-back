from app.dependencies import get_db_connection
from app.repositories.sqlalchemy import SqlalchemyInviteRepository
from fastapi import Depends

from ..invite_service import InviteService


def make_invite_service(session=Depends(get_db_connection)):
    invite_repository = SqlalchemyInviteRepository(session)
    return InviteService(invite_repository)
