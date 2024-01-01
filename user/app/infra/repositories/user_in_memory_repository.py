from faker import Faker

from app.application.repositories import UserRepository
from app.domain.entities.user import User


class UserInMemoryRepository(UserRepository):
    def __init__(self):
        self.database: list[User] = []
        self.faker = Faker()

    def list_all(self):
        return self.database

    def create(self, data) -> User:
        id = len(self.database) + 1

        user: User = {
            "id": id,
            "updated_at": self.faker.date_time(),
            "created_at": self.faker.date_time(),
            "auth_provider": None,
            "email": data["email"],
            "password": data["password"],
            "avatar_url": None,
            "name": data["name"],
            "notification_state": True,
        }

        self.database.append(user)

        return user

    def get_by_id(self, id):
        user = None

        for item in self.database:
            if item["id"] == id:
                user = item

        if user is not None:
            return user

        return None

    def get_by_email(self, email):
        user = None

        for item in self.database:
            if item["email"] == email:
                user = item

        if user is not None:
            return user

        return None

    def partial_update(self, id, data_to_update):
        user = None

        for item in self.database:
            if item["id"] == id:
                user = item

        if user is not None:
            for key, value in data_to_update.items():
                user[key] = value

            return user

        return None

    def delete(self, id):
        pass
