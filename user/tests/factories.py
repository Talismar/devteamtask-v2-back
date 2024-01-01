from faker import Faker
from sqlalchemy.orm import Session

from app.application.utils.cryptography import hash_password
from app.infra.repositories import (
    NotificationSqlalchemyRepository,
    UserSqlalchemyRepository,
)


class FactoriesMixin:
    def __call__(self, *args, **kwargs):
        self.faker: Faker
        self.session: Session

    def make_user(self):
        repository = UserSqlalchemyRepository(self.session)

        raw_password = self.faker.password()
        hasher_password = hash_password(raw_password)

        user_data = {
            "name": self.faker.name(),
            "email": self.faker.email(),
            "password": hasher_password,
        }

        user_data_created = repository.create(user_data)

        return user_data_created

    def make_notification(self, user_id: int):
        repository = NotificationSqlalchemyRepository(self.session)

        # user_data = {

        # }

        # notification_data_created = repository.create({""})
