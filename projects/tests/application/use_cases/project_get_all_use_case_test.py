from uuid import uuid1

import pytest
from sqlalchemy import text

from app.application.use_cases import ProjectGetAllUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import ProjectBaseTest


class TestProjectGetAllCase(ProjectBaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = ProjectGetAllUseCase(self.project_repository)

    def test_must_be_returns_an_empty_project_and_user_list(self):
        "Validar se é possivel obter a lista de projetos com todos os projetos que um usuário faz parte"

        projects = self.sut.execute(1)

        assert "projects" in projects
        assert projects["projects"] == []
        assert "users" in projects
        assert projects["users"] == []

    def test_must_be_returns_an_project_list_with_threes_items(self):
        self.make_user()
        self.make_project()
        self.make_project()
        self.make_project()

        projects = self.sut.execute(1)

        assert len(projects["projects"]) == 3
        assert len(projects["users"]) == 1

    def test_must_be_returns_an_empty_project_list(self):
        self.make_project()
        self.make_project()
        self.make_project()

        projects = self.sut.execute(2)

        assert len(projects["projects"]) == 0
        assert len(projects["users"]) == 0
