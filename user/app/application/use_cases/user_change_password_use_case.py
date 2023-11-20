from app.application.dtos import UserChangePasswordRequestDTO
from app.application.repositories import UserRepository
from app.application.utils.cryptography import hash_password, verify_password
from app.domain.entities.user import User
from app.domain.errors import BadRequestException, ResourceNotFoundException


class UserChangePasswordUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data: UserChangePasswordRequestDTO, request_user: User):
        user = request_user

        old_password = data.pop("old_password")

        if not verify_password(old_password, user["password"]):
            raise BadRequestException("Old Passwords do not match")

        data["new_password"] = hash_password(data["new_password"])

        user_updated = self.user_repository.partial_update(
            user["id"], {"password": data["new_password"]}
        )

        return user_updated
