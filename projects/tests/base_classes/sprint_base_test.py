from app.infra.repositories import (
    EventNotesSqlalchemyRepository,
    ProjectSqlalchemyRepository,
    SprintSqlalchemyRepository,
)
from tests.factories import FactoriesMixinToTesting

from .base_test import BaseTest


class SprintBaseTest(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.project_repository = ProjectSqlalchemyRepository(self.session)
        self.sprint_repository = SprintSqlalchemyRepository(self.session)
        self.event_notes_repository = EventNotesSqlalchemyRepository(self.session)
