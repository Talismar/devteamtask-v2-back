from abc import ABC, abstractmethod

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def list_all(self) -> list[User]:
        pass

    @abstractmethod
    def create(self, data: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> User | None:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    def partial_update(self, id: int, data_to_update: User) -> User:
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
