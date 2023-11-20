from fastapi import Depends

from app.application.use_cases import InviteCreateUseCase, InviteValidateByTokenUseCase
from app.infra.dependencies import database_connection
from app.infra.repositories import InviteSqlalchemyRepository, UserSqlalchemyRepository


def make_invite_create_use_case(session=Depends(database_connection)):
    invite_repository = InviteSqlalchemyRepository(session)
    return InviteCreateUseCase(invite_repository)


def make_invite_validate_by_token_use_case(session=Depends(database_connection)):
    invite_repository = InviteSqlalchemyRepository(session)
    user_repository = UserSqlalchemyRepository(session)
    return InviteValidateByTokenUseCase(invite_repository, user_repository)
