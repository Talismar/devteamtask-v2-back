import pytest

from app.application.use_cases import AuthenticationGenerateTokensUseCase
from app.application.utils.cryptography import hash_password
from app.domain.errors import UnauthorizedException
from app.infra.repositories import UserSqlalchemyRepository
from app.infra.utils.authentication_jwt import AuthenticationJWT
from tests.base_test import BaseTest


class TestAuthenticationGenerateTokensUseCase(BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.user_repository = UserSqlalchemyRepository(self.session)
        auth_jwt = AuthenticationJWT()
        self.sut = AuthenticationGenerateTokensUseCase(self.user_repository, auth_jwt)

    def test_it_must_be_possible_to_generate_authentication_tokens(self):
        email = "talismar.unal@gmail.com"
        raw_password = "asdasd"
        encryp_password = hash_password(raw_password)

        self.user_repository.create(
            {
                "name": "Talismar Fernandes Costa",
                "email": email,
                "password": encryp_password,
            }
        )

        user_jwt = self.sut.execute({"email": email, "password": raw_password})

        assert "access_token" in user_jwt
        assert "refresh_token" in user_jwt

    def test_it_must_return_an_error_for_user_that_does_not_exist(self):
        with pytest.raises(UnauthorizedException, match="Account already exists"):
            self.sut.execute(
                {"email": self.fake.email(), "password": self.fake.password()}
            )
