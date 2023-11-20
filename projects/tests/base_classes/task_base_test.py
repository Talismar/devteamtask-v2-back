from app.infra.repositories import StatusSqlalchemyRepository, TaskSqlalchemyRepository
from tests.factories import FactoriesMixinToTesting

from .base_test import BaseTest


class TaskBaseTest(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.task_repository = TaskSqlalchemyRepository(self.session)
