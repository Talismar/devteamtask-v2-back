import pytest

from app.application.use_cases import TaskDeleteUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import TaskBaseTest


class TestTaskDeleteCase(TaskBaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = TaskDeleteUseCase(self.task_repository)

    def test_task_delete_use_case(self):
        task = self.make_task()

        current_task_id = task.data_created["id"]

        was_deleted = self.sut.execute(current_task_id)

        assert was_deleted is None

    def test_should_throw_an_exception_when_try_delete_a_task_with_incorrect_id(
        self,
    ):
        with pytest.raises(ResourceNotFoundException, match="Task not found"):
            self.sut.execute(10)
