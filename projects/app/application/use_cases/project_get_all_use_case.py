from app.application.repositories import ProjectRepository


class ProjectGetAllUseCase:
    def __init__(self, project_repository: ProjectRepository) -> None:
        self.__project_repository = project_repository

    def execute(self, user_id: int):
        projects = self.__project_repository.get_all(user_id)
        users = []
        users_ids: set[int] = set()

        for index, project in enumerate(projects):
            users_ids.add(project["leader_id"])

            if project["product_owner_id"] is not None:
                users_ids.add(project["product_owner_id"])

            if len(project["collaborators_ids"]) > 0:
                users_ids.update(project["collaborators_ids"])

            if len(project["sprints"]) > 0:
                projects[index]["current_sprint"] = project["sprints"][0]
            else:
                projects[index]["current_sprint"] = None

        if len(users_ids) > 0:
            users = self.__project_repository.get_users_data(tuple(users_ids))  # type: ignore

        return {"projects": projects, "users": users}
