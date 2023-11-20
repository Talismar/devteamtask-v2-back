from uuid import uuid1

import pytest

from app.application.use_cases import ProjectDeleteUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import ProjectBaseTest


class TestProjectDeleteUseCase(ProjectBaseTest):
    def setup_method(self, method):
        super().setup_method(method)
        self.sut = ProjectDeleteUseCase(self.project_repository)

    def test_delete(self):
        "Deve ser possivel deletar um projeto"

        project = self.make_project()
        project_id = project.data_created["id"]

        self.sut.execute(project_id)

    def test_delete_exception(self):
        "Deve lançar uma exception quando o id do projeto não for encontrado"
        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(uuid1())
