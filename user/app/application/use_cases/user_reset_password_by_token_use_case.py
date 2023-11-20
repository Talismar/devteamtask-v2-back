from datetime import datetime

from app.application.dtos import UserResetPasswordByTokenRequestDTO
from app.application.repositories import InviteRepository, UserRepository
from app.application.utils.cryptography import hash_password
from app.domain.errors import BadRequestException, ResourceNotFoundException


class UserResetPasswordByTokenUseCase:
    def __init__(
        self, user_repository: UserRepository, invite_repository: InviteRepository
    ):
        self.user_repository = user_repository
        self.invite_repository = invite_repository

    def execute(self, data: UserResetPasswordByTokenRequestDTO):
        password_confirm = data.pop("password_confirm")
        invite_token = data.pop("invite_token")

        if data["password"] != password_confirm:
            raise BadRequestException("Passwords do not match")

        invite = self.invite_repository.get_by_token(invite_token)

        if invite is None:
            raise ResourceNotFoundException("Invite")

        current_today = datetime.now()

        if invite["expiration_date"] < current_today:
            self.invite_repository.delete(invite["id"])
            raise BadRequestException("Expiration date has passed")

        user = self.user_repository.get_by_email(invite["email"])

        if user is None:
            raise ResourceNotFoundException("User")

        data["password"] = hash_password(data["password"])

        user_updated = self.user_repository.partial_update(
            user["id"], {"password": data["password"]}
        )

        self.invite_repository.delete(invite["id"])

        return user_updated
