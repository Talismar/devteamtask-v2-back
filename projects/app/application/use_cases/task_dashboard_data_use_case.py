from app.application.repositories import TaskRepository


class TaskDashboardDataUseCase:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def execute(self, user_id: int):
        total_completed = self.task_repository.get_total_completed(user_id)
        total_assigned = self.task_repository.get_total_assigned(user_id)
        total_scheduled = self.task_repository.get_total_scheduled(user_id)
        total_task_in_last_7_days = self.task_repository.get_total_task_in_last_7_days(
            user_id
        )
        total_pending_in_last_7_days = (
            self.task_repository.get_total_pending_in_last_7_days(user_id)
        )
        total_completed_by_day_in_last_7_days = (
            self.task_repository.get_total_completed_in_last_7_days(user_id)
        )

        return {
            "total_completed": total_completed,
            "total_assigned": total_assigned,
            "total_scheduled": total_scheduled,
            "total_task_in_last_7_days": total_task_in_last_7_days,
            "total_pending_in_last_7_days": total_pending_in_last_7_days,
            "total_completed_by_day_in_last_7_days": total_completed_by_day_in_last_7_days,  # noqa: E501
        }
