from datetime import datetime, timedelta

from app.application.use_cases import DailyGetAllBySprintIdUseCase
from tests.base_classes import DailyBaseTest


class TestDailyGetAllUseCase(DailyBaseTest):
    def test_get_all_by_sprint_id(self):
        self.sut = DailyGetAllBySprintIdUseCase(self.daily_repository)

        project = self.make_project()
        sprint = self.make_sprint(project.data_created["id"])
        self.make_event_notes(sprint_id=sprint.data_created["id"])

        note_to_create = self.fake.paragraph()
        sprint_id = sprint.data_created["id"]
        self.daily_repository.create(sprint_id, {"note": note_to_create})

        daily_list = self.sut.execute(sprint_id)

        assert len(daily_list) == 1
        assert daily_list[0]["note"] == note_to_create
