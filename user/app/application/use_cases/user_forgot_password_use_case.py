from datetime import datetime, timedelta

from app.application.repositories import InviteRepository, UserRepository
from app.domain.errors import ResourceNotFoundException


class UserForgotPasswordUseCase:
    def __init__(
        self, user_repository: UserRepository, invite_repository: InviteRepository
    ):
        self.user_repository = user_repository
        self.invite_repository = invite_repository

    def execute(self, email: str):
        user_storaged = self.user_repository.get_by_email(email)

        if user_storaged is None:
            raise ResourceNotFoundException("User")

        current_date = datetime.now()
        one_day = timedelta(days=1)
        expiration_date = current_date + one_day

        invite = self.invite_repository.create(
            {
                "resource_name": "User",
                "resource_id": str(user_storaged["id"]),
                "expiration_date": expiration_date,
                "email": email,
            }
        )

        return invite
