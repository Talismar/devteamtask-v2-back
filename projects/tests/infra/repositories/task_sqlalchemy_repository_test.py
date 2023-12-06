from uuid import uuid1

import pytest

from app.domain.errors import ResourceNotFoundException
from app.infra.repositories import TaskSqlalchemyRepository
from tests.base_classes import BaseTest
from tests.factories import FactoriesMixinToTesting


class TestTaskSqlalchemyRepository(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = TaskSqlalchemyRepository(self.session)

    def test_task_create(self):
        "Deve ser possivel criar uma tarefa"
        project = self.make_project()
        project_id = project.data_created["id"]

        task = self.sut.create(
            {
                "project_id": project_id,
                "created_by_user_id": 1,
                "description": "Description",
                "name": "Name",
                "status_id": 1,
                "priority": 1,
            },
            [],
        )

        assert task["id"] == 1
        assert task["status"]["name"] == "TO DO"

    def test_task_get_by_id(self):
        "Deve ser possivel obter os dados de uma tarefa pelo seu id"
        task = self.make_task()

        task_retrieve = self.sut.get_by_id(task.data_created["id"])

        assert task_retrieve.id == task.data_created["id"]
        assert task_retrieve.status.name == "TO DO"

    def test_partial_update(self):
        "Deve ser possivel atualizar os dados de uma tarefa"
        task = self.make_task()

        description_to_update = self.fake.name()
        task_retrieve = self.sut.partial_update(
            task.data_created["id"], {"description": description_to_update}
        )

        assert task_retrieve.description == description_to_update

    def test_partial_update_2(self):
        "Deve lançar uma exceção quando tentar atualizar uma tarefa com um id incorreto"

        with pytest.raises(ResourceNotFoundException):
            description_to_update = self.fake.name()
            self.sut.partial_update(1, {"description": description_to_update})

    def test_get_by_id(self):
        "Deve retornar none quando tenta buscar uma tarefa com um id incorreto"
        task_retrieve = self.sut.get_by_id(10)

        assert task_retrieve is None

    def test_delete(self):
        "Deve lançar uma exceção quando tentar deletar uma tarefa com um id incorreto"
        with pytest.raises(ResourceNotFoundException):
            self.sut.delete(10)
