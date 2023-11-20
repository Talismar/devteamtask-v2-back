from typing import Any
from uuid import uuid1

import pytest

from app.application.use_cases import StatusGetAllUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import StatusBaseTest


class TestStatusGetAllUseCase(StatusBaseTest):
    def test_get_all(self):
        "Deve ser possivel obter todos os status"
        self.make_status("To do")

        self.sut = StatusGetAllUseCase(self.status_repository)
        status_list = self.sut.execute()

        assert type(status_list) is list
        assert status_list[0].name == "To do"
