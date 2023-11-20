from typing import Any
from uuid import uuid1

import pytest

from app.application.use_cases import TagGetByIdUseCase
from app.domain.errors import ResourceNotFoundException
from tests.base_classes import TagBaseTest


class TestTagGetByIdUseCase(TagBaseTest):
    def setup_method(self, method):
        super().setup_method(method)
        self.sut = TagGetByIdUseCase(self.tag_repository)

    def test_get_by_id(self):
        "Deve ser possivel obter um tag por id"

        tag = self.make_tag("User")
        tag_id = tag.data_created.id

        tag_retrieve = self.sut.execute(tag_id)

        assert tag_retrieve.name == "User"

    def test_get_by_id_2(self):
        "Deve lançar uma exception quando o id de um tag não existir"

        with pytest.raises(ResourceNotFoundException):
            self.sut.execute(5)
