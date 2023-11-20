from app.application.repositories import (
    EventNotesRepository,
    ProjectRepository,
    SprintRepository,
)
from app.domain.errors import BusinessRuleException, ResourceNotFoundException


class SprintCreateUseCase:
    def __init__(
        self,
        sprint_repository: SprintRepository,
        project_repository: ProjectRepository,
        event_notes_repository: EventNotesRepository,
    ) -> None:
        self.__sprint_repository = sprint_repository
        self.__project_repository = project_repository
        self.__event_notes_repository = event_notes_repository

    def execute(self, user_id: int, data: dict):
        try:
            project = self.__project_repository.get_by_id(data["project_id"])

            if project is None:
                raise ResourceNotFoundException("Project")

            if project["leader_id"] != user_id:
                raise BusinessRuleException("You are not allowed to create a sprint")

            sprint = self.__sprint_repository.create(data)

            self.__event_notes_repository.create({"sprint_id": sprint["id"]})

            return sprint

        except Exception as e:
            raise e
