from app.domain.errors import BusinessRuleException, ResourceNotFoundException

from ..interfaces.repositories import ProjectRepository, SprintRepository


class SprintCreateUseCase:
    def __init__(
        self, sprint_repository: SprintRepository, project_repository: ProjectRepository
    ) -> None:
        self.__sprint_repository = sprint_repository
        self.__project_repository = project_repository

    def execute(self, user_id: int, data: dict):
        try:
            project_instance = self.__project_repository.get_by_id(data["project_id"])

            if project_instance is None:
                raise ResourceNotFoundException("Project")

            if project_instance["project_data"]["leader_id"] != user_id:
                raise BusinessRuleException("You are not allowed to create a sprint")

            return self.__sprint_repository.create(data)

        except Exception as e:
            raise e
