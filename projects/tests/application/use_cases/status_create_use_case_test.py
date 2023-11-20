from uuid import uuid1

import pytest

from app.application.use_cases import StatusCreateUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import StatusBaseTest


class TestStatusCreateUseCase(StatusBaseTest):
    def test_create(self):
        self.sut = StatusCreateUseCase(self.status_repository, self.project_repository)

        project = self.make_project()
        project_id = project.data_created["id"]

        name = "User"
        status = self.sut.execute({"name": name, "project_id": project_id})

        assert status.name == name

    def test_create_2(self):
        self.sut = StatusCreateUseCase(self.status_repository, self.project_repository)

        with pytest.raises(ResourceNotFoundException):
            name = "User"
            self.sut.execute({"name": name, "project_id": uuid1()})
