from app.infra.repositories import ProjectSqlalchemyRepository, TagSqlalchemyRepository
from tests.factories import FactoriesMixinToTesting

from .base_test import BaseTest


class TagBaseTest(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.project_repository = ProjectSqlalchemyRepository(self.session)
        self.tag_repository = TagSqlalchemyRepository(self.session)
