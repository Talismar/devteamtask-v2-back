from uuid import uuid1

import pytest

from app.application.use_cases import ProjectAddCollaboratorUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import ProjectBaseTest


class TestProjectAddCollaboratorUseCase(ProjectBaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = ProjectAddCollaboratorUseCase(self.project_repository)

    def test_add_collaborator(self):
        user = self.make_user()
        project = self.make_project()

        project_id = project.data_created["id"]
        user_id = user["user_id"]

        ret = self.sut.execute(project_id, user_id)

        assert ret == "Added"

    def test_add_collaborator_with_incorret_project_id(self):
        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(uuid1(), 1)
