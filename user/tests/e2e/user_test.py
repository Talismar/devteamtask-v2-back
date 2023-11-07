from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_db_connection
from app.models.base_model import BaseModel
from app.configs.test import engine
from httpx import Response
from tests.dependencies import override_get_db


client = TestClient(app)


app.dependency_overrides[get_db_connection] = override_get_db


class TestE2EUserService:
    def reset_database(self):
        BaseModel.metadata.drop_all(engine)
        BaseModel.metadata.create_all(engine)

    def test_should_be_possible_to_create_user(self):
        self.reset_database()

        response = self.create_user()

        assert response.status_code == 201

    def test_should_be_possible_to_list_users_for_authenticated_user(self):
        self.reset_database()

        for i in range(5):
            response = self.create_user(f"talismar{i}.una@gmail.com")

        access_token = self.get_access_token("talismar0.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }
        response = client.get("/user", headers=headers).json()

        assert len(response) == 5

    def test_should_be_possible_to_update_name_of_user(self):
        self.reset_database()

        self.create_user()
        access_token = self.get_access_token("talismar.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        json_data = {"name": "Antonio"}
        response = client.patch("/user/1", json=json_data, headers=headers)

        assert response.status_code == 200
        assert response.json()["name"] == "Antonio"

    def test_should_be_possible_to_delete_user(self):
        self.reset_database()

        self.create_user()
        access_token = self.get_access_token("talismar.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        response = client.delete("/user/1", headers=headers)

        assert response.status_code == 204

    def test_should_be_possible_to_get_a_user(self):
        self.reset_database()

        self.create_user()
        access_token = self.get_access_token("talismar.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        response = client.get("/user/1", headers=headers)

        assert response.status_code == 200
        assert response.json()["email"] == "talismar.una@gmail.com"
        assert "Talismar " in response.json()["name"]

    def create_user(self, email: str = "talismar.una@gmail.com"):
        data = {
            "name": "Talismar Fernandes Costa",
            "email": email,
            "password": "12345678",
            "password_confirm": "12345678",
        }

        response_create = client.post("/user", json=data)
        return response_create

    def get_access_token(self, email, password):
        json_data = {"email": email, "password": password}
        response: Response = client.post("/authentication/token", json=json_data)
        return response.json()["access_token"]
