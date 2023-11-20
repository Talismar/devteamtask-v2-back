import pytest

from app.application.use_cases import TaskDashboardDataUseCase
from app.domain.errors import ResourceNotFoundException
from app.infra.repositories import ProjectSqlalchemyRepository
from tests.base_classes import TaskBaseTest


class TestTaskDashboardDataUseCase(TaskBaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = TaskDashboardDataUseCase(self.task_repository)

    def test_task_dashboard_data_use_case(self):
        data = self.sut.execute(1)

        assert "total_completed" in data
        assert "total_assigned" in data
        assert "total_scheduled" in data
        assert "total_task_in_last_7_days" in data
        assert "total_pending_in_last_7_days" in data
        assert "total_completed_by_day_in_last_7_days" in data

    def test_must_return_data_for_a_specific_user(
        self,
    ):
        task = self.make_task()
        user = self.make_user(2)

        project_repository = ProjectSqlalchemyRepository(self.session)

        project_repository.add_collaborator(
            task.data_to_create["project_id"], user["user_id"]
        )

        self.make_task(assigned_to_user_id=user["user_id"])

        data = self.sut.execute(1)

        assert data["total_scheduled"] == 1
        assert data["total_task_in_last_7_days"] == 1
