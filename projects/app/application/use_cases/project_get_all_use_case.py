from ..interfaces.repositories import ProjectRepository


class ProjectGetAllUseCase:
    def __init__(self, project_repository: ProjectRepository) -> None:
        self.__project_repository = project_repository

    def execute(self, user_id: int):
        results = self.__project_repository.get_all(user_id)
        return results
