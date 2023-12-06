from uuid import uuid1

import pytest

from app.domain.errors import ResourceNotFoundException
from app.infra.repositories import TagSqlalchemyRepository
from tests.base_classes import BaseTest
from tests.factories import FactoriesMixinToTesting


class TestTagSqlalchemyRepository(FactoriesMixinToTesting, BaseTest):
    def setup_method(self, method):
        super().setup_method(method)

        self.sut = TagSqlalchemyRepository(self.session)

    def test_create(self):
        "Deve ser possivel criar um tag"
        tag = self.make_tag("User")

        assert tag.data_created.name == "User"

    def test_create_2(self):
        "Não deve criar outra tag se caso existe alguma com o mesmo nome"
        tag1 = self.make_tag("User")
        tag2 = self.make_tag("User")

        assert tag1.data_created.id == 1
        assert tag2.data_created.id == 1

    def test_get_all(self):
        "Deve ser possivel obter a lista de tags"
        tags = self.sut.get_all()

        assert tags == []

    def test_get_by_id(self):
        "Deve ser possivel obter os dados de uma tag pelo seu id"
        self.make_tag("User")

        tag_retrieve = self.sut.get_by_id(1)
        assert tag_retrieve.id == 1
        assert tag_retrieve.name == "User"

    def test_delete(self):
        "Deve ser possivel deletar uma tag que não esteja vinculada a nenhum projeto"
        self.make_tag("User")

        tag_retrieve = self.sut.delete(1)
        assert tag_retrieve is None

    def test_returns_none(self):
        "Deve retorna none quando tenta busca uma tag que não existe"
        tag_retrieve = self.sut.get_by_id(10)

        assert tag_retrieve is None
