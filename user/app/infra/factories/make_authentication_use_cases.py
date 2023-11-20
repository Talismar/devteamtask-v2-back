from fastapi import Depends

from app.application.use_cases import (
    AuthenticationByProviderUseCase,
    AuthenticationGenerateTokensUseCase,
    AuthenticationRefreshTokenUseCase,
)
from app.infra.dependencies import database_connection
from app.infra.repositories import UserSqlalchemyRepository
from app.infra.utils.authentication_jwt import authentication_jwt


def make_authentication_token_use_case(session=Depends(database_connection)):
    repository = UserSqlalchemyRepository(session)
    use_case = AuthenticationGenerateTokensUseCase(repository, authentication_jwt)
    return use_case


def make_refresh_token_use_case():
    use_case = AuthenticationRefreshTokenUseCase(authentication_jwt)
    return use_case


def make_authentication_by_provider_use_case(session=Depends(database_connection)):
    repository = UserSqlalchemyRepository(session)
    use_case = AuthenticationByProviderUseCase(repository, authentication_jwt)
    return use_case
