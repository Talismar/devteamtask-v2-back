from app.application.repositories import DailyRepository


class DailyGetByIdUseCase:
    def __init__(self, repository: DailyRepository) -> None:
        self.repository = repository

    def execute(self, id: int):
        return self.repository.get_by_id(id)
