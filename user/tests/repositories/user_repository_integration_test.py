from app.infra.repositories import UserSqlalchemyRepository
from tests.base_test import BaseTest


class TestUserRepositoryIntegration(BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = UserSqlalchemyRepository(self.session)

    def test_it_must_be_possible_to_obtain_the_data_of_a_registered_user(self):
        name = self.faker.name()
        email = self.faker.email()
        id = 1

        self.sut.create(
            {
                "name": name,
                "email": email,
                "password": "asdasd",
            }
        )

        user_data = self.sut.get_by_id(id)

        assert user_data["id"] == id
        assert user_data["email"] == email
        assert user_data["name"] == name

    def test_must_return_none_when_the_user_does_not_exist(
        self,
    ):
        name = self.faker.name()
        email = self.faker.email()

        self.sut.create(
            {
                "name": name,
                "email": email,
                "password": "asdasd",
            }
        )

        user_data = self.sut.get_by_id(10)

        assert user_data is None
