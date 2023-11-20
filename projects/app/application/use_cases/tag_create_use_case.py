from app.application.dtos import TagRequestDTO
from app.application.repositories import ProjectRepository, TagRepository
from app.domain.errors import ResourceNotFoundException


class TagCreateUseCase:
    def __init__(
        self, tag_repository: TagRepository, project_repository: ProjectRepository
    ) -> None:
        self.__tag_repository = tag_repository
        self.__project_repository = project_repository

    def execute(self, data: TagRequestDTO):
        project_id = data.pop("project_id")

        tag_instance = self.__tag_repository.get_or_create(data)
        try:
            self.__project_repository.add_tag_status(project_id, tag_instance, "tags")
        except ResourceNotFoundException as e:
            raise e

        return {"id": tag_instance.id, "name": tag_instance.name}
