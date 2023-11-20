from app.application.dtos import StatusRequestDTO
from app.application.repositories import ProjectRepository, StatusRepository
from app.domain.entities.status import Status


class StatusCreateUseCase:
    def __init__(
        self, status_repository: StatusRepository, project_repository: ProjectRepository
    ) -> None:
        self.__status_repository = status_repository
        self.project_repository = project_repository

    def execute(self, data: StatusRequestDTO):
        project_id = data.pop("project_id")

        status = self.__status_repository.get_or_create(data)
        try:
            self.project_repository.add_tag_status(project_id, status, "status")
            return status
        except Exception as exception:
            raise exception
