from uuid import uuid1

import pytest

from app.application.use_cases import TaskCreateUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import TaskBaseTest


class TestTaskCreateCase(TaskBaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = TaskCreateUseCase(self.task_repository)

    def test_should_throw_an_exception_when_register_a_task_with_project_id_incorrect(
        self,
    ):
        self.make_project()
        with pytest.raises(ResourceNotFoundException, match="Project not found"):
            self.sut.execute(
                {
                    "project_id": uuid1(),
                    "created_by_user_id": 1,
                    "description": "Description",
                    "name": "Name",
                    "status_id": 1,
                    "priority": 1,
                    "tags_ids": [],
                }
            )

    def test_task_create_use_case(self):
        project = self.make_project()
        project_id = project.data_created["id"]

        task = self.sut.execute(
            {
                "project_id": project_id,
                "created_by_user_id": 1,
                "description": "Description",
                "name": "Name",
                "status_id": project.data_created["status"][0]["id"],
                "priority": 1,
                "tags_ids": [],
            }
        )

        assert task["id"] == 1
        assert task["status"]["name"] == "TO DO"
