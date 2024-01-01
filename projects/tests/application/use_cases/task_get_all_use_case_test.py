from app.application.use_cases import TaskGetAllUseCase
from tests.base_classes import TaskBaseTest


class TestTaskGetAllUseCase(TaskBaseTest):
    def test_get_all(self):
        "Deve ser possivel obter todos as tasks"
        name = "Task fake name"
        task = self.make_task(name=name)

        self.sut = TaskGetAllUseCase(self.task_repository)
        task_list = self.sut.execute(task.data_to_create["project_id"], None)

        assert type(task_list) is list
        assert task_list[0].name == name
