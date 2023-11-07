from datetime import datetime, timedelta
from uuid import UUID

from app.application.interfaces.repositories import TaskRepository
from app.domain.errors import ResourceNotFoundException
from app.infra.database.models import StatusModel, TaskModel
from sqlalchemy import func, text, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class TaskSqlalchemyRepository(TaskRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, data: dict):
        try:
            new_data = TaskModel(**data)

            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return new_data
        except IntegrityError as e:
            raise ResourceNotFoundException(
                e.args[0].split("is not present in table")[1].split('"')[1].capitalize()
            )

    def get_all(self):
        data = self.__session.query(TaskModel).all()
        return data

    def get_by_id(self, id: int):
        data = self.__session.query(TaskModel).get(id)
        return data

    def partial_update(self, id: int, data: dict):
        # self.__session.query(TaskModel).filter(TaskModel.id == id).update(data)
        update_statement = (
            update(TaskModel)
            .where(TaskModel.id == id)
            .values(**data)
            .returning(
                TaskModel.id,
                TaskModel.name,
                TaskModel.description,
                TaskModel.created_at,
                TaskModel.updated_at,
                TaskModel.priority,
                TaskModel.status_id,
            )
        )

        result = self.__session.execute(update_statement)
        dict_of_results = {
            key: value for key, value in zip(result.keys(), result.fetchall()[0])
        }
        self.__session.commit()
        return dict_of_results

    def delete(self, id: int):
        data = self.__session.get(TaskModel, id)

        if data is not None:
            self.__session.delete(data)
            self.__session.commit()
            return True

        return False

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

        query = self.__session.query(TaskModel).filter(
            TaskModel.assigned_to_user_id == user_id,
            TaskModel.status == status_instance,
            TaskModel.updated_at >= seven_days_ago,
        )

        def total_by_date(date):
            return query.filter(func.date(TaskModel.updated_at) == date.date()).count()

        data = []

        for item in query:
            date = item.updated_at.date()
            amount = total_by_date(date)
            data.append({"date": date, "amount": amount})

        return data

    def get_total_pending_in_last_7_days(self, user_id):
        status_instance = self.get_status_by_name("To do")
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
