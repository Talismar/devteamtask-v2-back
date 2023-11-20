from app.application.use_cases import TagGetAllUseCase
from tests.base_classes import TagBaseTest


class TestTagGetAllUseCase(TagBaseTest):
    def test_get_all(self):
        "Deve ser possivel obter todos as tags"
        self.make_tag("User")

        self.sut = TagGetAllUseCase(self.tag_repository)
        tag_list = self.sut.execute()

        assert type(tag_list) is list
        assert tag_list[0].name == "User"
