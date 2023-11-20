from app.application.use_cases import EventNotesGetByIdUseCase
from tests.base_classes import EventNotesBaseTest


class TestEventNotesGetByIdUseCase(EventNotesBaseTest):
    def test_get_by_sprint_id(self):
        self.sut = EventNotesGetByIdUseCase(self.event_notes_repository)

        project = self.make_project()
        project_id = project.data_created["id"]

        sprint = self.make_sprint(project_id=project_id)
        sprint_id = sprint.data_created["id"]

        event_notes = self.make_event_notes(sprint_id=sprint_id)

        event_notes_retrieve = self.sut.execute(sprint_id)

        assert event_notes_retrieve["planning"] == event_notes.data_created["planning"]
        assert (
            event_notes_retrieve["retrospective"]
            == event_notes.data_created["retrospective"]
        )
        assert event_notes_retrieve["review"] == event_notes.data_created["review"]
        assert event_notes_retrieve["id"] == event_notes.data_created["id"]
