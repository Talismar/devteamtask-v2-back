from datetime import datetime, timedelta

from app.application.use_cases import ProjectCreateUseCase
from tests.base_classes import ProjectBaseTest


class TestProjectCreateUseCase(ProjectBaseTest):
    def test_project_create_use_case(self):
        self.make_status("TO DO")
        self.make_status("DOING")
        self.make_status("DONE")

        self.sut = ProjectCreateUseCase(self.project_repository, self.status_repository)

        end_date = self.fake.date_time_between(
            start_date=datetime.now(), end_date=datetime.now() + timedelta(days=30)
        )
        project = self.sut.execute(
            {"name": "Project name", "end_date": end_date, "leader_id": 1}
        )

        assert len(project["status"]) >= 3
        assert project["leader_id"] == 1
