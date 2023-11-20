from abc import ABC, abstractmethod
from uuid import UUID

from app.domain.entities.invite import Invite


class InviteRepository(ABC):
    @abstractmethod
    def create(self, data: Invite) -> Invite:
        pass

    @abstractmethod
    def get_by_token(self, token: UUID) -> Invite:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
