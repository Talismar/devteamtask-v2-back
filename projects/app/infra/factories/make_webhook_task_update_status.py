from fastapi import Depends

from app.application.use_cases import WebhookTaskUpdateStatusUseCase
from app.infra.repositories import TaskSqlalchemyRepository

from ..dependencies import database_connection


def make_webhook_task_update_status(session=Depends(database_connection)):
    repository = TaskSqlalchemyRepository(session)
    use_case = WebhookTaskUpdateStatusUseCase(repository)
    return use_case
