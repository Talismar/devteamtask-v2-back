from datetime import datetime
from typing import TypedDict
from uuid import UUID

from app.application.repositories import InviteRepository, UserRepository
from app.domain.entities.invite import Invite
from app.domain.entities.user import User
from app.domain.errors import (
    BadRequestException,
    DatabaseException,
    ResourceNotFoundException,
)


class ResponseDTO(TypedDict):
    invite: Invite
    user: User


class InviteValidateByTokenUseCase:
    def __init__(
        self, invite_repository: InviteRepository, user_repository: UserRepository
    ):
        self.invite_repository = invite_repository
        self.user_repository = user_repository

    def execute(self, token: UUID) -> ResponseDTO:
        try:
            invite = self.invite_repository.get_by_token(token)

            if invite is None:
                raise ResourceNotFoundException("Invite")

            current_today = datetime.now()

            if invite["expiration_date"] <= current_today:
                raise BadRequestException("Expiration date has passed")

            user = self.user_repository.get_by_email(invite["email"])

            if user is None:
                raise ResourceNotFoundException("User")

            return {"invite": invite, "user": user}
        except DatabaseException:
            raise BadRequestException("Error creating notification")
