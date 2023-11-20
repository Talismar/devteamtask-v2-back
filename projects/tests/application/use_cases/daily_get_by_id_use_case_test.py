from datetime import datetime, timedelta

from app.application.use_cases import DailyGetByIdUseCase
from tests.base_classes import DailyBaseTest


class TestDailyGetByIdUseCase(DailyBaseTest):
    def test_get_by_id(self):
        self.sut = DailyGetByIdUseCase(self.daily_repository)

        project = self.make_project()
        sprint = self.make_sprint(project.data_created["id"])
        self.make_event_notes(sprint_id=sprint.data_created["id"])

        note_to_create = self.fake.paragraph()
        sprint_id = sprint.data_created["id"]
        daily = self.daily_repository.create(sprint_id, {"note": note_to_create})

        daily_retrieve = self.sut.execute(daily["id"])

        assert daily_retrieve["note"] == note_to_create
