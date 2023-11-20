from uuid import uuid1

import pytest

from app.domain.errors import ResourceNotFoundException
from app.infra.repositories import StatusSqlalchemyRepository
from tests.base_classes import BaseTest
from tests.factories import FactoriesMixinToTesting


class TestStatusSqlalchemyRepository(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = StatusSqlalchemyRepository(self.session)

    def test_status_create(self):
        status = self.make_status("TO DO")

        assert status.data_created.name == "TO DO"

    def test_status_get_by_id(self):
        self.make_status("TO DO")

        status_retrieve = self.sut.get_by_id(1)
        assert status_retrieve.id == 1

    def test_returns_none(self):
        status_retrieve = self.sut.get_by_id(10)

        assert status_retrieve is None
