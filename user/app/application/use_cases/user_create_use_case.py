from app.application.dtos import UserCreateRequestDTO
from app.application.repositories.user_repository import UserRepository
from app.application.utils.cryptography import hash_password
from app.domain.errors import BadRequestException


class UserCreateUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data: UserCreateRequestDTO):
        if data["password"] != data["password_confirm"]:
            raise BadRequestException("Passwords do not match")

        data.pop("password_confirm")

        data["password"] = hash_password(data["password"])

        return self.user_repository.create(data)
