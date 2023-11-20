from app.application.repositories import DailyRepository
from app.domain.entities.daily import Daily


class DailyCreateUseCase:
    def __init__(self, repository: DailyRepository) -> None:
        self.repository = repository

    def execute(self, sprint_id: int, data: Daily):
        return self.repository.create(sprint_id, data)
