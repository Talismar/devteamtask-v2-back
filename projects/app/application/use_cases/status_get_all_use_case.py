from app.application.repositories import StatusRepository


class StatusGetAllUseCase:
    def __init__(self, status_repository: StatusRepository) -> None:
        self.__status_repository = status_repository

    def execute(self):
        return self.__status_repository.get_all()
