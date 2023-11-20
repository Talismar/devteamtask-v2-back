from app.infra.repositories import (
    ProjectSqlalchemyRepository,
    StatusSqlalchemyRepository,
    TagSqlalchemyRepository,
)
from tests.factories import FactoriesMixinToTesting

from .base_test import BaseTest


class ProjectBaseTest(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.project_repository = ProjectSqlalchemyRepository(self.session)
        self.status_repository = StatusSqlalchemyRepository(self.session)
        self.tag_repository = TagSqlalchemyRepository(self.session)
