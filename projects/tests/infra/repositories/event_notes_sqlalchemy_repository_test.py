from uuid import uuid1

import pytest

from app.domain.errors import ResourceNotFoundException
from app.infra.repositories import EventNotesSqlalchemyRepository
from tests.base_classes import BaseTest
from tests.factories import FactoriesMixinToTesting


class TestEventNotesSqlalchemyRepository(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = EventNotesSqlalchemyRepository(self.session)

    def test_event_notes_create(self):
        "Deve ser possivel criar uma event note apartir do id de uma sprint"
        project = self.make_project()
        sprint = self.make_sprint(project.data_created["id"])

        sprint_id = sprint.data_created["id"]

        planning = self.fake.text()
        event_notes = self.make_event_notes(sprint_id=sprint_id, planning=planning)

        assert event_notes.data_created["id"] == 1
        assert event_notes.data_created["sprint_id"] == sprint_id
        assert event_notes.data_created["planning"] == planning

    def test_create_2(self):
        "Deve lançar uma exceção quando tentar criar uma event note com um sprint id incorreto"

        with pytest.raises(ResourceNotFoundException):
            self.make_event_notes(sprint_id=15)

    def test_get_by_sprint_id(self):
        "Deve ser possivel obter os dado de uma event note aparti do seu id"
        project = self.make_project()
        sprint = self.make_sprint(project.data_created["id"])

        sprint_id = sprint.data_created["id"]
        self.make_event_notes(sprint_id=sprint_id)

        event_notes_retrieve = self.sut.get_by_sprint_id(sprint_id)

        assert event_notes_retrieve["sprint_id"] == sprint_id
        assert "planning" in event_notes_retrieve
        assert "retrospective" in event_notes_retrieve
        assert "review" in event_notes_retrieve

    def test_get_by_sprint_id_2(self):
        "Deve lançar uma exceção quando tentar buscar uma event note com um sprint id incorreto"

        with pytest.raises(ResourceNotFoundException):
            self.sut.get_by_sprint_id(1)

    def test_partial_update(self):
        "Deve ser possivel atualizar os dados de uma event note"
        project = self.make_project()
        sprint = self.make_sprint(project.data_created["id"])

        sprint_id = sprint.data_created["id"]
        event_notes = self.make_event_notes(sprint_id=sprint_id)

        review_to_update = self.fake.name()
        event_notes_retrieve = self.sut.partial_update(
            event_notes.data_created["id"], {"review": review_to_update}
        )

        assert event_notes_retrieve["review"] == review_to_update

    def test_partial_update_2(self):
        "Deve lançar uma exceção quando tentar atualizar uma event note com um id incorreto"

        with pytest.raises(ResourceNotFoundException):
            self.sut.partial_update(1, {})
