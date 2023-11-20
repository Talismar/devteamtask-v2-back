from uuid import uuid1

import pytest

from app.domain.errors import ResourceNotFoundException
from app.infra.repositories import SprintSqlalchemyRepository
from tests.base_classes import BaseTest
from tests.factories import FactoriesMixinToTesting


class TestSprintSqlalchemyRepository(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = SprintSqlalchemyRepository(self.session)

    def test_create(self):
        project = self.make_project()
        sprint = self.make_sprint(
            project_id=project.data_created["id"], name="Sprint 1"
        )

        assert sprint.data_created["name"] == "Sprint 1"
        assert isinstance(sprint.data_created["description"], str) is True

    def test_create_2(self):
        "Deve lançar uma exceção quando tenta criar uma sprint com um projeto que não existe"
        with pytest.raises(ResourceNotFoundException):
            self.make_sprint(project_id=uuid1(), name="Sprint 1")

    def test_partial_update(self):
        "Deve ser possivel editar dados da sprint"
        project = self.make_project()

        sprint_name_to_create = "Sprint 1"
        sprint = self.make_sprint(
            project_id=project.data_created["id"], name=sprint_name_to_create
        )

        sprint_name_to_update = "Sprint Update"
        sprint_retrieve = self.sut.partial_update(
            sprint.data_created["id"], {"name": sprint_name_to_update}
        )

        assert sprint_retrieve["name"] != sprint_name_to_create
