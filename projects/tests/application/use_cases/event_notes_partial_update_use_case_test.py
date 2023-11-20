from app.application.use_cases import EventNotesPartialUpdateUseCase
from tests.base_classes import EventNotesBaseTest


class TestEventNotesPartialUpdateUseCase(EventNotesBaseTest):
    def test_partial_update(self):
        self.sut = EventNotesPartialUpdateUseCase(self.event_notes_repository)

        project = self.make_project()
        project_id = project.data_created["id"]

        sprint = self.make_sprint(project_id=project_id)
        sprint_id = sprint.data_created["id"]

        event_notes = self.make_event_notes(sprint_id=sprint_id)

        event_notes_id = event_notes.data_created["id"]

        planning = self.fake.paragraph()
        review = self.fake.paragraph()
        event_notes_retrieve = self.sut.execute(
            event_notes_id, {"planning": planning, "review": review}
        )

        assert event_notes_retrieve["planning"] == planning
        assert (
            event_notes_retrieve["retrospective"]
            == event_notes.data_created["retrospective"]
        )
        assert event_notes_retrieve["review"] == review
