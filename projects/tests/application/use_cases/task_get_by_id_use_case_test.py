from typing import Any
from uuid import uuid1

import pytest

from app.application.use_cases import TaskGetByIdUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import TaskBaseTest


class TestTaskGetByIdUseCase(TaskBaseTest):
    def setup_method(self, method):
        super().setup_method(method)
        self.sut = TaskGetByIdUseCase(self.task_repository)

    def test_get_by_id(self):
        "Deve ser possivel obter um tag por id"

        task_name = "Task name"
        task = self.make_task(name=task_name)
        task_id = task.data_created["id"]

        task_retrieve = self.sut.execute(task_id)

        assert task_retrieve.name == task_name

    def test_get_by_id_2(self):
        "Deve lançar uma exception quando o id de um task não existir"

        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(5)
