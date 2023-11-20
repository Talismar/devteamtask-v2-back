import pytest

from app.application.use_cases import UserForgotPasswordUseCase
from app.application.utils.cryptography import hash_password
from app.domain.errors import BadRequestException
from app.infra.repositories import InviteSqlalchemyRepository, UserSqlalchemyRepository
from app.infra.utils.authentication_jwt import AuthenticationJWT
from tests.base_test import BaseTest


class TestForgotPasswordUseCaseIntegration(BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.user_repository = UserSqlalchemyRepository(self.session)
        invite_repository = InviteSqlalchemyRepository(self.session)
        self.sut = UserForgotPasswordUseCase(self.user_repository, invite_repository)

    def test_it_must_be_possible_to_update_password_of_user_application(self):
        pass
