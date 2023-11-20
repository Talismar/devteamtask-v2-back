import pytest

from app.application.use_cases import TaskPartialUpdateUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import TaskBaseTest


class TestTaskPartialUpdateCase(TaskBaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = TaskPartialUpdateUseCase(self.task_repository)

    def test_task_partial_update_use_case(self):
        task = self.make_task()

        current_task_name = task.data_to_create["name"]
        current_task_description = task.data_to_create["description"]

        task_updated = self.sut.execute(
            task.data_created["id"], {"name": self.fake.name()}
        )

        assert task_updated.name != current_task_name
        assert task_updated.description == current_task_description

    def test_should_throw_an_exception_when_try_update_a_task_with_incorrect_id(
        self,
    ):
        with pytest.raises(ResourceNotFoundException, match="Task not found"):
            self.sut.execute(10, {"name": ""})
