from uuid import uuid1

import pytest

from app.application.abstract_media_storages import AbstractMediaStorages
from app.application.use_cases import ProjectGetByIdUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import ProjectBaseTest


class FakeStorages(AbstractMediaStorages):
    def save_file(self, new_file, original_filename):
        return original_filename

    def get_url_media(self, filename: str):
        return filename


class TestProjectGetByIdUseCase(ProjectBaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        storages = FakeStorages()
        self.sut = ProjectGetByIdUseCase(self.project_repository, storages)

    def test_should_throw_an_exception_when_fetching_a_project_with_incorrect_id(self):
        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(uuid1())

    def test_it_should_be_possible_to_get_a_project_by_id(self):
        self.make_user()
        self.make_user(2)
        self.make_user(3)
        project = self.make_project(product_owner_id=3, logo_url="fake.png")
        project_id = project.data_created["id"]

        self.project_repository.add_collaborator(project_id, 2)

        project_detail = self.sut.execute(project_id)

        assert project_detail["project_data"]["id"] == project_id
