from app.application.use_cases import DailyPartialUpdateUseCase
from tests.base_classes import DailyBaseTest


class TestDailyPartialUpdateUseCase(DailyBaseTest):
    def test_partial_update(self):
        self.sut = DailyPartialUpdateUseCase(self.daily_repository)

        project = self.make_project()
        sprint = self.make_sprint(project.data_created["id"])
        self.make_event_notes(sprint_id=sprint.data_created["id"])

        note_to_create = self.fake.paragraph()
        sprint_id = sprint.data_created["id"]
        daily_created = self.daily_repository.create(
            sprint_id, {"note": note_to_create}
        )

        note_to_update = self.fake.paragraph()
        daily_updated = self.sut.execute(daily_created["id"], {"note": note_to_update})

        assert daily_updated["note"] != note_to_create
        assert daily_updated["note"] == note_to_update
