from datetime import datetime, timedelta
from uuid import UUID

from app.application.repositories import TaskRepository
from app.domain.errors import ResourceNotFoundException
from app.infra.database.models import ProjectModel, StatusModel, TagModel, TaskModel
from sqlalchemy import func, text, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, load_only

from .mapper.task_sqlalchemy_mapper import TaskSqlalchemyMapper


class TaskSqlalchemyRepository(TaskRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, data, tags_ids: list[int]):
        try:
            new_data = TaskModel(**data)

            tags = (
                self.__session.query(TagModel).filter(TagModel.id.in_(tags_ids)).all()
            )

            for tag in tags:
                new_data.tags.add(tag)

            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return TaskSqlalchemyMapper.toDomain(new_data)
        except IntegrityError as e:
            raise ResourceNotFoundException(
                e.args[0].split("is not present in table")[1].split('"')[1].capitalize()
            )

    def get_all_by_project_id(self, project_id, task_name):
        if task_name is not None:
            data = (
                self.__session.query(TaskModel)
                .filter(
                    TaskModel.project_id == project_id,
                    TaskModel.name.icontains(task_name),
                )
                .all()
            )
        else:
            data = (
                self.__session.query(TaskModel).filter_by(project_id=project_id).all()
            )
        return data

    def get_by_id(self, id: int):
        data = self.__session.get(TaskModel, id)
        return data

    def partial_update(self, id: int, data: dict):
        tags_ids = data.pop("tags_ids", None)

        task_instance = self.__session.get(TaskModel, id)

        if task_instance is None:
            raise ResourceNotFoundException("Task")

        if tags_ids is not None:
            if len(tags_ids) > 0:
                tags_instance = (
                    self.__session.query(TagModel)
                    .filter(TagModel.id.in_(tags_ids))
                    .all()
                )

                for tag in tags_instance:
                    task_instance.tags.add(tag)

            elif len(tags_ids) == 0:
                task_instance.tags.clear()

        for key, value in data.items():
            setattr(task_instance, key, value)

        self.__session.commit()
        self.__session.refresh(task_instance)

        return task_instance

    def update_status_by_id_and_project_id(self, task_id, project_id, status_name):
        task_instance = self.get_by_id(task_id)

        if task_instance is not None and project_id == task_instance.project_id:
            project_instance = (
                self.__session.query(ProjectModel).filter_by(id=project_id).first()
            )

            status_instance = None

            for item in project_instance.status:
                if item.name == status_name:
                    status_instance = item

            task_instance.status = status_instance

            self.__session.commit()
            self.__session.refresh(task_instance)

            return task_instance

    def delete(self, id: int):
        data = self.__session.get(TaskModel, id)

        if data is not None:
            self.__session.delete(data)
            self.__session.commit()
            return True

        raise ResourceNotFoundException("Task")

    def get_status_by_name(self, name: str):
        status_instance = self.__session.query(StatusModel).filter_by(name=name).first()
        return status_instance

    def get_total_completed(self, user_id):
        status_instance = self.get_status_by_name("Done")
        task_amount = (
            self.__session.query(TaskModel)
            .filter_by(status=status_instance, assigned_to_user_id=user_id)
            .count()
        )
        return task_amount

    def get_total_assigned(self, user_id):
        task_amount = (
            self.__session.query(TaskModel)
            .filter_by(assigned_to_user_id=user_id)
            .count()
        )
        return task_amount

    def get_total_completed_in_last_7_days(self, user_id):
        status_instance = self.get_status_by_name("Done")
        seven_days_ago = datetime.now() - timedelta(days=7)

        query = (
            self.__session.query(TaskModel)
            .filter(
                TaskModel.assigned_to_user_id == user_id,
                TaskModel.status == status_instance,
                TaskModel.updated_at >= seven_days_ago,
            )
            .all()
        )

        def total_by_date(date):
            return (
                self.__session.query(TaskModel)
                .filter(func.date(TaskModel.updated_at) == date)
                .count()
            )

        data = []

        for item in query:
            date = item.updated_at.date()
            amount = total_by_date(date)
            data.append({"date": date, "amount": amount})

        return data

    def get_total_pending_in_last_7_days(self, user_id):
        status_instance = self.get_status_by_name("To Do")
        seven_days_ago = datetime.now() - timedelta(days=7)
        task_amount = (
            self.__session.query(TaskModel)
            .filter(
                (TaskModel.status == status_instance)
                & (TaskModel.assigned_to_user_id == user_id)
                & (TaskModel.updated_at >= seven_days_ago)
            )
            .count()
        )
        return task_amount

    def get_total_task_in_last_7_days(self, user_id):
        seven_days_ago = datetime.now() - timedelta(days=7)

        query = """
        SELECT COUNT(*)
        FROM task
        WHERE (
            project_id IN (
                SELECT id
                FROM project
                WHERE leader_id = :user_id
                OR :user_id IN (
                    SELECT user_id
                    FROM projectcollaborator
                    WHERE project_id = project.id
                )
                OR product_owner_id = :user_id
            )
            AND assigned_to_user_id IS NULL
            AND updated_at >= :seven_days_ago
        )
        """

        params = {
            "user_id": user_id,
            "seven_days_ago": seven_days_ago,
        }

        result = self.__session.execute(text(query), params)

        task_amount = result.scalar()
        return task_amount

    def get_total_scheduled(self, user_id):
        query = """
        SELECT COUNT(*)
        FROM task
        WHERE (
            project_id IN (
                SELECT id
                FROM project
                WHERE leader_id = :user_id
                OR :user_id IN (
                    SELECT user_id
                    FROM projectcollaborator
                    WHERE project_id = project.id
                )
                OR product_owner_id = :user_id
            )
            AND assigned_to_user_id IS NULL
        )
        """

        params = {
            "user_id": user_id,
        }
        result = self.__session.execute(text(query), params)

        task_amount = result.scalar()
        return task_amount
