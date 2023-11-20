from app.application.repositories import DailyRepository
from app.domain.entities.daily import Daily


class DailyPartialUpdateUseCase:
    def __init__(self, repository: DailyRepository) -> None:
        self.repository = repository

    def execute(self, id: int, data: Daily):
        return self.repository.partial_update(id, data)
