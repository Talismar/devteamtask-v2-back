from uuid import uuid1

import pytest

from app.application.use_cases import TagCreateUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import TagBaseTest


class TestTagCreateUseCase(TagBaseTest):
    def setup_method(self, method):
        super().setup_method(method)
        self.sut = TagCreateUseCase(self.tag_repository, self.project_repository)

    def test_create(self):
        project = self.make_project()
        project_id = project.data_created["id"]

        name = "User"
        tag = self.sut.execute({"name": name, "project_id": project_id})

        assert tag["name"] == name

    def test_create_2(self):
        "Deve lançar uma exception quanto tentar criar uma tag com project id incorreto"

        with pytest.raises(ResourceNotFoundException):
            name = "User"
            self.sut.execute({"name": name, "project_id": uuid1()})
