from fastapi import Depends

from app.application.use_cases import ProjectCreateUseCase
from app.infra.repositories import (
    ProjectSqlalchemyRepository,
    StatusSqlalchemyRepository,
)
from app.infra.utils import SendEmailService

from ..dependencies import database_connection


def make_project_create(session=Depends(database_connection)):
    send_email_service = SendEmailService("Project")
    project_repository = ProjectSqlalchemyRepository(session)
    status_repository = StatusSqlalchemyRepository(session)
    use_case = ProjectCreateUseCase(
        project_repository, status_repository, send_email_service
    )
    return use_case
