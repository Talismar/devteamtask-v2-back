from uuid import uuid1

import pytest

from app.domain.errors import ResourceNotFoundException
from app.infra.repositories import ProjectSqlalchemyRepository
from tests.base_classes import BaseTest
from tests.factories import FactoriesMixinToTesting


class TestProjectSqlalchemyRepository(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = ProjectSqlalchemyRepository(self.session)

    def test_create(self):
        "Deve ser possivel criar um projeto"
        project_name = "Project name"
        project = self.make_project(name=project_name)

        assert project.data_created["name"] == project_name
        assert project.data_created["logo_url"] is None
        assert project.data_created["leader_id"] == 1

    def test_get_by_id(self):
        "Deve ser possivel obter os dados de um projeto aparti do seu id"
        project = self.make_project()

        project_retrieve = self.sut.get_by_id(project.data_created["id"])

        assert "name" in project_retrieve
        assert "status" in project_retrieve

    def test_should_returns_none_if_project_not_exists(self):
        "Deve retorna none se o id do projeto não existir"
        project_retrieve = self.sut.get_by_id(uuid1())

        assert project_retrieve is None

    def test_it_should_be_possible_to_delete_a_project(self):
        "Deve ser possivel para o usúario que criou deleta um projeto"
        project = self.make_project()
        project_id = project.data_created["id"]

        was_deleted = self.sut.delete(project_id)

        assert was_deleted is None

    def test_should_throw_an_exception_when_try_delete_a_project_with_incorrect_id(
        self,
    ):
        with pytest.raises(ResourceNotFoundException):
            self.sut.delete(uuid1())
