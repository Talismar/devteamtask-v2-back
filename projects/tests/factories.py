from datetime import datetime, timedelta
from typing import Any, Generic, TypeVar
from uuid import UUID

from faker import Faker
from sqlalchemy import text
from sqlalchemy.orm import Session
from typing_extensions import Unpack

from app.domain.entities.event_notes import EventNotes
from app.domain.entities.project import Project
from app.domain.entities.sprint import Sprint
from app.infra.repositories import (
    EventNotesSqlalchemyRepository,
    ProjectSqlalchemyRepository,
    SprintSqlalchemyRepository,
    StatusSqlalchemyRepository,
    TagSqlalchemyRepository,
    TaskSqlalchemyRepository,
)

T1 = TypeVar("T1")
T2 = TypeVar("T2")


class MakeResourceReturn(Generic[T1, T2]):
    def __init__(self, data_to_create: T1, data_created: T2) -> None:
        self.data_to_create = data_to_create
        self.data_created = data_created


class FactoriesMixinToTesting:
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.fake: Faker
        self.session: Session

    def make_project(self, **kwargs: Unpack[Project]):  # type: ignore
        repository = ProjectSqlalchemyRepository(self.session)

        current_date = datetime.now()
        after_date = timedelta(days=30) + current_date

        status = set(
            (
                self.make_status("TO DO").data_created,
                self.make_status("DOING").data_created,
                self.make_status("DONE").data_created,
            )
        )

        data_to_create = {
            "name": self.fake.name(),
            "end_date": self.fake.date_time_between(
                start_date=current_date, end_date=after_date
            ),
            "leader_id": 1,
            "status": status,
            **kwargs,
        }

        data_created = repository.create(data_to_create)

        return MakeResourceReturn(data_to_create, data_created)

    def make_status(self, name=None):
        repository = StatusSqlalchemyRepository(self.session)

        data_to_create = {"name": self.fake.name()}

        data_created = repository.get_or_create(
            {"name": name} if name is not None else data_to_create
        )

        return MakeResourceReturn(data_to_create, data_created)

    def make_tag(self, name=None):
        repository = TagSqlalchemyRepository(self.session)

        data_to_create = {"name": self.fake.name()}

        data_created = repository.get_or_create(
            {"name": name} if name is not None else data_to_create
        )

        return MakeResourceReturn(data_to_create, data_created)

    def make_task(self, **kwargs):
        repository = TaskSqlalchemyRepository(self.session)

        project = self.make_project()
        project_id = project.data_created["id"]

        task_to_create = {
            "project_id": project_id,
            "created_by_user_id": 1,
            "description": self.fake.name(),
            "name": self.fake.name(),
            "status_id": 1,
            "priority": 1,
            **kwargs,
        }

        task_created = repository.create(
            task_to_create,
            [],
        )

        return MakeResourceReturn(task_to_create, task_created)

    def make_user(self, user_id=1):
        data_to_create = {
            "user_id": user_id,
            "user_name": self.fake.name(),
            "user_email": self.fake.email(),
            "user_password": self.fake.password(),
            "user_created_at": self.fake.date_time_between(),
            "user_updated_at": self.fake.date_time_between(),
        }

        self.session.execute(
            text(
                """insert into users (id, name, email, password, created_at, updated_at) 
                   values (:user_id, :user_name, :user_email, :user_password, :user_created_at, :user_updated_at) 
                   RETURNING *"""
            ),
            params=data_to_create,
        )

        self.session.commit()
        self.session.close()
        # for index, row in enumerate(data.keys()):
        # data.fetchone()

        return data_to_create

    def make_sprint(self, project_id: UUID, **kwargs: Unpack[Sprint]):  # type: ignore
        data_to_create = {
            "name": self.fake.name(),
            "description": self.fake.name(),
            "project_id": project_id,
            **kwargs,
        }

        repository = SprintSqlalchemyRepository(self.session)

        data_created = repository.create(data_to_create)

        return MakeResourceReturn(data_to_create, data_created)

    def make_event_notes(self, sprint_id: int, **kwargs: Unpack[EventNotes]):  # type: ignore
        data_to_create = {"sprint_id": sprint_id, **kwargs}

        repository = EventNotesSqlalchemyRepository(self.session)

        data_created = repository.create(data_to_create)

        return MakeResourceReturn(data_to_create, data_created)
