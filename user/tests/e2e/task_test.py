from fastapi.testclient import TestClient
from app.main import app
from app.dependencies import get_db_connection
from app.models.base_model import BaseModel
from app.configs.test import engine
from tests.dependencies import override_get_db
from httpx import Response

client = TestClient(app)


app.dependency_overrides[get_db_connection] = override_get_db


class TestE2ETaskService:
    def reset_database(self):
        BaseModel.metadata.drop_all(engine)
        BaseModel.metadata.create_all(engine)

    def test_should_be_possible_to_create_a_task_for_authenticated_user(self):
        self.reset_database()

        self.create_user()
        access_token = self.get_access_token("talismar.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        json_data = {"name": "Task name", "description": "Task description"}
        response = client.post("/task", json=json_data, headers=headers)

        assert response.status_code == 201
        assert response.json()["name"] == "Task name"
        assert response.json()["description"] == "Task description"

    def test_should_be_possible_to_list_tasks_for_authenticated_user(self):
        self.reset_database()

        self.create_user()
        access_token = self.get_access_token("talismar.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        json_data = {"name": "Task name", "description": "Task description"}
        client.post("/task", json=json_data, headers=headers)
        response = client.get("/task", headers=headers).json()

        assert len(response) == 1

    def test_should_be_possible_to_update_task(self):
        self.reset_database()

        self.create_user()
        access_token = self.get_access_token("talismar.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        json_data = {"name": "Task name", "description": "Task description"}
        client.post("/task", json=json_data, headers=headers)
        json_updated_data = {"name": "Task name updated"}
        response = client.patch("/task/1", headers=headers, json=json_updated_data)

        assert response.status_code == 200
        assert response.json()["name"] == json_updated_data["name"]
        assert response.json()["description"] == "Task description"

    def test_should_be_possible_to_delete_user(self):
        self.reset_database()

        self.create_user()
        access_token = self.get_access_token("talismar.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        json_data = {"name": "Task name", "description": "Task description"}
        client.post("/task", json=json_data, headers=headers)
        response = client.delete("/task/1", headers=headers)

        assert response.status_code == 204

    def test_should_be_possible_to_get_a_task_for_authenticated_user(self):
        self.reset_database()

        self.create_user()
        access_token = self.get_access_token("talismar.una@gmail.com", "12345678")
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        json_data = {"name": "Task name", "description": "Task description"}
        client.post("/task", json=json_data, headers=headers)

        response = client.get("/task/1", headers=headers)

        assert response.status_code == 200
        assert response.json()["name"] == "Task name"

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
