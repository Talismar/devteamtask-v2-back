from app.application.repositories.user_repository import UserRepository


class UserDeleteUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: int):
        return self.user_repository.delete(user_id)
