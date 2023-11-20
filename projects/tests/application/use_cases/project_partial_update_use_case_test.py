from uuid import uuid1

import pytest
from sqlalchemy import text
from starlette.datastructures import UploadFile

from app.application.abstract_email_service import AbstractEmailService
from app.application.abstract_media_storages import AbstractMediaStorages
from app.application.use_cases import ProjectPartialUpdateUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import ProjectBaseTest


class FakeStorages(AbstractMediaStorages):
    def save_file(self, new_file, original_filename):
        return f"{uuid1()}-{new_file.filename}"

    def get_url_media(self, filename: str):
        return filename


class FakeEmailService(AbstractEmailService):
    def send(self, emails, resource_id, redirect_path):
        pass


class FakeEmailServiceWithException(AbstractEmailService):
    def send(self, emails, resource_id, redirect_path):
        raise Exception("Failed to send")


class TestProjectPartialUpdateCase(ProjectBaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        storages = FakeStorages()
        email_service = FakeEmailService()
        self.sut = ProjectPartialUpdateUseCase(
            self.project_repository, storages, email_service
        )

    def test_partial_update(self):
        "Deve ser possivel atualizar o nome e a logo de um projeto"
        self.make_user()
        project = self.make_project()

        project_id = project.data_created["id"]
        name_to_update = "Project Name"
        logo_url = UploadFile(b"", filename="logo.png")
        project_updated = self.sut.execute(
            project_id, {"name": name_to_update, "logo_url": logo_url}
        )

        assert project_updated["project_data"]["name"] == name_to_update
        assert logo_url.filename in project_updated["project_data"]["logo_url"]

    def test_partial_update_2(self):
        "Deve lançar uma exception quando tenta atualizar um project com um id incorreto"
        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(uuid1(), {})

    def test_partial_update_3(self):
        "Deve retornar os dados do projeto quando tentar atualizar um projeto sem passar nenhum dado"
        self.make_user()
        project = self.make_project()

        project_id = project.data_created["id"]

        project_ret = self.sut.execute(project_id, {})

        assert "id" in project_ret["project_data"]
        assert "name" in project_ret["project_data"]
        assert "end_date" in project_ret["project_data"]
        assert "start_date" in project_ret["project_data"]

    def test_partial_update_4(self):
        "Deve ser possivel atualizar product_owner e collaborators de um projeto"
        self.make_user()
        project = self.make_project()

        project_id = project.data_created["id"]
        product_owner_email = self.fake.email()
        collaborators_emails = [self.fake.email()]

        project_updated = self.sut.execute(
            project_id,
            {
                "collaborator_emails": collaborators_emails,
                "product_owner_email": product_owner_email,
            },
        )

        assert project_updated["project_data"]["id"] == project_id

    def test_partial_update_5(self):
        "Deve lidar com exception de envio de email quando tentar atualizar product_owner de um projeto"
        self.make_user()
        project = self.make_project()

        project_id = project.data_created["id"]
        product_owner_email = self.fake.email()

        self.sut.email_service = FakeEmailServiceWithException()

        with pytest.raises(Exception):
            self.sut.execute(
                project_id,
                {
                    "product_owner_email": product_owner_email,
                },
            )

    def test_partial_update_6(self):
        "Deve lidar com exception de envio de email quando tentar atualizar product_owner de um projeto"
        self.make_user()
        project = self.make_project()

        project_id = project.data_created["id"]
        collaborators_emails = [self.fake.email()]

        self.sut.email_service = FakeEmailServiceWithException()

        with pytest.raises(Exception):
            self.sut.execute(
                project_id,
                {
                    "collaborator_emails": collaborators_emails,
                },
            )
