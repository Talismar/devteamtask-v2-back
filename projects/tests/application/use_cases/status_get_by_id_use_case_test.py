from typing import Any
from uuid import uuid1

import pytest

from app.application.use_cases import StatusGetByIdUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import StatusBaseTest


class TestStatusGetByIdUseCase(StatusBaseTest):
    def setup_method(self, method):
        super().setup_method(method)
        self.sut = StatusGetByIdUseCase(self.status_repository)

    def test_get_by_id(self):
        "Deve ser possivel obter um status por id"

        status = self.make_status(1, "To do")
        status_id = status.data_created.id

        status_retrieve = self.sut.execute(status_id)

        assert status_retrieve.name == "To do"

    def test_get_by_id_2(self):
        "Deve lançar uma exception quando o id de um status não existir"

        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(5)
