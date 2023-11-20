from uuid import uuid1

import pytest

from app.application.use_cases import SprintCreateUseCase
from app.domain.errors import BusinessRuleException, ResourceNotFoundException
from tests.base_classes import SprintBaseTest


class TestSprintCreateUseCase(SprintBaseTest):
    def setup_method(self, method):
        super().setup_method(method)
        self.sut = SprintCreateUseCase(
            self.sprint_repository, self.project_repository, self.event_notes_repository
        )

    def test_create(self):
        "Deve ser possivel criar uma sprint"
        project = self.make_project()
        project_id = project.data_created["id"]
        name = self.fake.name()
        description = self.fake.name()

        sprint = self.sut.execute(
            1,
            {
                "name": name,
                "description": description,
                "project_id": project_id,
            },
        )

        assert sprint["name"] == name
        assert sprint["description"] == description
        assert sprint["project_id"] == project_id

    def test_create_2(self):
        "Deve lançar uma exception quando tentar criar uma sprint com um id de projeto incorreto"

        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(
                1,
                {
                    "name": "Fake name",
                    "description": "Fake description",
                    "project_id": uuid1(),
                },
            )

    def test_create_3(self):
        "Deve lançar uma exception quando um usuário que não é leader do projeto tentar criar uma sprint"

        with pytest.raises(
            BusinessRuleException, match="You are not allowed to create a sprint"
        ):
            project = self.make_project()
            self.sut.execute(
                5,
                {
                    "name": "Fake name",
                    "description": "Fake description",
                    "project_id": project.data_created["id"],
                },
            )
