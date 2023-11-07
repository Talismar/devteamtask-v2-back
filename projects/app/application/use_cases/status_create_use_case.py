from ..interfaces.repositories import StatusRepository


class StatusCreateUseCase:
    def __init__(self, status_repository: StatusRepository) -> None:
        self.__status_repository = status_repository

    def execute(self, data):
        return self.__status_repository.get_or_create(data)
