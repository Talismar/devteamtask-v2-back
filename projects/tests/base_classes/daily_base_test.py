from app.infra.repositories import DailySqlalchemyRepository
from tests.factories import FactoriesMixinToTesting

from .base_test import BaseTest


class DailyBaseTest(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.daily_repository = DailySqlalchemyRepository(self.session)
