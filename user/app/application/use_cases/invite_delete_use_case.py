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


class InviteDeleteUseCase:
    def __init__(self, invite_repository: InviteRepository):
        self.invite_repository = invite_repository

    def execute(self, id: int):
        self.invite_repository.delete(id)
