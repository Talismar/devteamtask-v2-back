from app.application.dtos import ProjectCreateRequestDTO
from app.application.repositories import ProjectRepository, StatusRepository


class ProjectCreateUseCase:
    def __init__(
        self, project_repository: ProjectRepository, status_repository: StatusRepository
    ) -> None:
        self.__project_repository = project_repository
        self.__status_repository = status_repository

    def execute(self, data: ProjectCreateRequestDTO):
        status = set()
        product_owner_email = data.pop("product_owner_email", None)
        collaborators_email = data.pop("collaborators_email", None)

        if product_owner_email is not None:
            # TODO: Implement Send email to product owner
            pass

        if collaborators_email is not None:
            # TODO: Implement Send email to collaborators
            pass

        # TODO: Optimize this
        for i in [1, 2, 3]:
            instance = self.__status_repository.get_by_id(i)
            if instance:
                status.add(instance)

        data.update({"status": status})
        return self.__project_repository.create(data)
