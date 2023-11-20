from app.application.dtos import InviteCreateRequestDTO
from app.application.repositories.invite_repository import InviteRepository
from app.domain.entities.invite import Invite
from app.domain.errors import BadRequestException, DatabaseException


class InviteCreateUseCase:
    def __init__(self, invite_repository: InviteRepository):
        self.invite_repository = invite_repository

    def execute(self, data: InviteCreateRequestDTO, emails: list[str]):
        results: list[Invite] = []

        for email in emails:
            try:
                invite = self.invite_repository.create({"email": email, **data})
                results.append(invite)
            except DatabaseException:
                raise BadRequestException("Error creating notification")

        return results
