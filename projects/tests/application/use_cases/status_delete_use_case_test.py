from typing import Any
from uuid import uuid1

import pytest

from app.application.use_cases import StatusDeleteUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import StatusBaseTest


class TestStatusDeleteUseCase(StatusBaseTest):
    def setup_method(self, method):
        super().setup_method(method)
        self.sut = StatusDeleteUseCase(self.status_repository)

    def test_delete(self):
        "Deve ser possivel deletar um status"

        status = self.make_status("To do")
        status_id = status.data_created.id

        status_deleted = self.sut.execute(status_id)

        assert status_deleted == "Status deleted successfully"

    def test_delete_2(self):
        "Deve lançar uma exception quando o id de um status não existir"

        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(5)
