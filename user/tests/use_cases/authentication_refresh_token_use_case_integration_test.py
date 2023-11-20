import pytest

from app.application.use_cases import (
    AuthenticationGenerateTokensUseCase,
    AuthenticationRefreshTokenUseCase,
)
from app.application.utils.cryptography import hash_password
from app.domain.errors import BadRequestException
from app.infra.repositories import UserSqlalchemyRepository
from app.infra.utils.authentication_jwt import AuthenticationJWT
from tests.base_test import BaseTest


class TestAuthenticationRefreshTokenUseCaseIntegration(BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.user_repository = UserSqlalchemyRepository(self.session)
        auth_jwt = AuthenticationJWT()
        self.authentication_generate_tokens_use_case = (
            AuthenticationGenerateTokensUseCase(self.user_repository, auth_jwt)
        )
        self.sut = AuthenticationRefreshTokenUseCase(auth_jwt)

    def test_it_must_be_possible_to_revalidate_the_expired_authentication_token(self):
        email = "talismar.una@gmail.com"
        raw_password = "asdasd"
        encryp_password = hash_password(raw_password)

        self.user_repository.create(
            {
                "name": "Talismar Fernandes Costa",
                "email": email,
                "password": encryp_password,
            }
        )

        user_jwt = self.authentication_generate_tokens_use_case.execute(
            {"email": email, "password": raw_password}
        )

        refresh_token = user_jwt["refresh_token"]

        new_tokens = self.sut.execute(refresh_token)

        assert "access_token" in new_tokens
        assert "refresh_token" in new_tokens
