from datetime import datetime, timedelta

from app.application.use_cases import DailyCreateUseCase
from tests.base_classes import DailyBaseTest


class TestDailyCreateUseCase(DailyBaseTest):
    def test_create(self):
        "Deve ser possivel criar uma daily"
        self.sut = DailyCreateUseCase(self.daily_repository)

        project = self.make_project()
        sprint = self.make_sprint(project.data_created["id"])
        self.make_event_notes(sprint_id=sprint.data_created["id"])

        note = self.fake.paragraph()
        sprint_id = sprint.data_created["id"]
        daily = self.sut.execute(sprint_id, {"note": note})

        assert daily["note"] == note
