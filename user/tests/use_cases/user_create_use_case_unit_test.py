import pytest

from app.application.use_cases import UserCreateUseCase
from app.application.utils.cryptography import verify_password
from app.domain.errors import BadRequestException
from app.infra.repositories import UserInMemoryRepository


class TestUserCreateUseCase:
    def setup_method(self, method):
        repository = UserInMemoryRepository()
        self.sut = UserCreateUseCase(repository)

    def test_it_must_be_possible_to_create_a_user(self):
        name = "Talismar Fernandes Costa"
        email = "talismar.unal@gmail.com"

        user_data = self.sut.execute(
            {
                "name": name,
                "email": email,
                "password": "asdasd",
                "password_confirm": "asdasd",
            }
        )

        assert user_data["id"] == 1
        assert user_data["name"] == name
        assert user_data["email"] == email

    def test_validate_whether_the_registered_password_was_encrypted(self):
        password = "asdasd"

        user_data = self.sut.execute(
            {
                "name": "Talismar Fernandes Costa",
                "email": "talismar.una@gmail.com",
                "password": password,
                "password_confirm": password,
            }
        )

        assert verify_password(password, user_data["password"]) is True

    def test_validate_whether_an_error_occurs_when_the_password_and_password_confirm_are_different(
        self,
    ):
        password = "asdasd"
        password_confirm = "asd"

        with pytest.raises(BadRequestException, match="Passwords do not match"):
            self.sut.execute(
                {
                    "name": "Talismar Fernandes Costa",
                    "email": "talismar.una@gmail.com",
                    "password": password,
                    "password_confirm": password_confirm,
                }
            )
