from app.application.repositories import TagRepository
from app.domain.errors import ResourceNotFoundException


class TagGetByIdUseCase:
    def __init__(self, tag_repository: TagRepository) -> None:
        self.__tag_repository = tag_repository

    def execute(self, id):
        data = self.__tag_repository.get_by_id(id)

        if data is None:
            raise ResourceNotFoundException("Tag")

        return data
