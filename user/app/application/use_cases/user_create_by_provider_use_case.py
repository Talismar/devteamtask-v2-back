from app.application.dtos import UserCreateByProviderRequestDTO
from app.application.repositories.user_repository import UserRepository


class UserCreateByProviderUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, data: UserCreateByProviderRequestDTO):
        login: str = data.pop("login")
        name = data.get("name", None)

        if name is None:
            data["name"] = login

        return self.user_repository.create({**data, "password": ""})
