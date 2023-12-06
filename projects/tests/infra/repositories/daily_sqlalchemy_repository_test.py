import pytest

from app.domain.errors import ResourceNotFoundException
from app.infra.repositories import DailySqlalchemyRepository
from tests.base_classes import BaseTest
from tests.factories import FactoriesMixinToTesting


class TestDailySqlalchemyRepository(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = DailySqlalchemyRepository(self.session)

    def test_create(self):
        "Deve ser possivel criar uma daily apartir do id de uma sprint que contenha um event note associada"
        project = self.make_project()
        project_id = project.data_created["id"]
        sprint = self.make_sprint(project_id=project_id)
        sprint_id = sprint.data_created["id"]
        self.make_event_notes(sprint_id=sprint_id)

        daily = self.sut.create(sprint_id, {})

        assert "note" in daily
        assert "created_at" in daily
        assert "updated_at" in daily

    def test_get_by_id(self):
        "Deve ser possivel obter os dado de uma daily"
        project = self.make_project()
        project_id = project.data_created["id"]
        sprint = self.make_sprint(project_id=project_id)
        sprint_id = sprint.data_created["id"]
        self.make_event_notes(sprint_id=sprint_id)

        daily = self.sut.create(sprint_id, {})

        daily_retrieve = self.sut.get_by_id(daily["id"])
        assert daily_retrieve["id"] == 1

    def test_partial_update(self):
        "Deve ser possivel atualizar os dados de uma daily"
        project = self.make_project()
        project_id = project.data_created["id"]
        sprint = self.make_sprint(project_id=project_id)
        sprint_id = sprint.data_created["id"]
        self.make_event_notes(sprint_id=sprint_id)

        note_to_create = self.fake.text()
        daily = self.sut.create(sprint_id, {"note": note_to_create})

        note_to_update = self.fake.text()
        daily_retrieve_after_updated = self.sut.partial_update(
            daily["id"], {"note": note_to_update}
        )

        assert daily_retrieve_after_updated["note"] == note_to_update

    def test_get_all_by_sprint_id(self):
        "Deve ser possivel obter todas as daily criadas em uma determinada sprint/event notes"
        project = self.make_project()
        project_id = project.data_created["id"]
        sprint = self.make_sprint(project_id=project_id)
        sprint_id = sprint.data_created["id"]
        self.make_event_notes(sprint_id=sprint_id)

        daily = self.sut.create(sprint_id, {"note": self.fake.text()})

        daily_datas = self.sut.get_all_by_sprint_id(sprint_id)

        assert daily in daily_datas
        assert len(daily_datas) == 1

    def test_returns_none(self):
        "Deve retorna um error ao tentar busca um daily com um id que não existe"
        with pytest.raises(ResourceNotFoundException):
            self.sut.get_by_id(10)
