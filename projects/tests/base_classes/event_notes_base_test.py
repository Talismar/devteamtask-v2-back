from app.infra.repositories import EventNotesSqlalchemyRepository
from tests.factories import FactoriesMixinToTesting

from .base_test import BaseTest


class EventNotesBaseTest(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.event_notes_repository = EventNotesSqlalchemyRepository(self.session)
