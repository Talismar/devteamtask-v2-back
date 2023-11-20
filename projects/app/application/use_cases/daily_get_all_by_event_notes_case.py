from app.application.repositories import DailyRepository


class DailyGetAllBySprintIdUseCase:
    def __init__(self, repository: DailyRepository) -> None:
        self.repository = repository

    def execute(self, sprint_id: int):
        return self.repository.get_all_by_sprint_id(sprint_id)
