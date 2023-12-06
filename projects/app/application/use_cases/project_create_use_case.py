from app.application.abstract_email_service import AbstractEmailService
from app.application.dtos import ProjectCreateRequestDTO
from app.application.repositories import ProjectRepository, StatusRepository


class ProjectCreateUseCase:
    def __init__(
        self,
        project_repository: ProjectRepository,
        status_repository: StatusRepository,
        email_service: AbstractEmailService,
    ) -> None:
        self.__project_repository = project_repository
        self.__status_repository = status_repository
        self.email_service = email_service

    def execute(self, data: ProjectCreateRequestDTO):
        status = set()
        product_owner_email = data.pop("product_owner_email", None)
        collaborators_email = data.pop("collaborators_email", None)

        # TODO: Optimize this
        for i in [1, 2, 3]:
            instance = self.__status_repository.get_by_id(i)
            if instance:
                status.add(instance)

        data.update({"status": status})

        project = self.__project_repository.create(data)  # type: ignore

        if product_owner_email is not None:
            try:
                self.email_service.send(
                    [product_owner_email],
                    str(project["id"]),
                    "add_product_owner",
                )
            except Exception as e:
                raise e

        if collaborators_email is not None:
            try:
                self.email_service.send(
                    collaborators_email,
                    str(project["id"]),
                    "add_collaborator",
                )
            except Exception as e:
                raise e

        return project
