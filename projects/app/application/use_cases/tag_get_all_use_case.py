from ..interfaces.repositories import TagRepository


class TagGetAllUseCase:
    def __init__(self, tag_repository: TagRepository) -> None:
        self.__tag_repository = tag_repository

    def execute(self):
        return self.__tag_repository.get_all()
