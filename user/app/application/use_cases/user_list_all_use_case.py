from app.application.repositories.user_repository import UserRepository
from app.domain.entities.user import User


class UserListAllUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def list_all(self) -> list[User]:
        return self.user_repository.list_all()
