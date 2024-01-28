from typing import Literal
from uuid import UUID

from app.application.repositories import ProjectRepository
from app.domain.errors import ResourceNotFoundException
from app.infra.database.models import (
    ProjectCollaboratorModel,
    ProjectModel,
    SprintModel,
    StatusModel,
    TagModel,
    TaskModel,
)
from app.infra.database.utils import attribute_names
from sqlalchemy import and_, asc, func, or_, text, update
from sqlalchemy.orm import Session, joinedload

from .mapper.project_sqlalchemy_mapper import ProjectSqlalchemyMapper


class ProjectSqlalchemyRepository(ProjectRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, data):
        status = set()

        for i, name in enumerate(["To Do", "Doing", "Done"], start=1):
            instance = StatusModel(name=name, order=i)
            if instance:
                status.add(instance)

        data.update({"status": status})

        new_data = ProjectModel(**data)

        try:
            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return ProjectSqlalchemyMapper.toDomain(new_data)
        except Exception as e:
            raise e

    def get_users_data(self, users_ids):
        params = {"users_ids": users_ids}
        query = "SELECT id, name, email, avatar_url, auth_provider FROM users WHERE id IN :users_ids;"
        result = self.__session.execute(text(query), params)
        results = []

        for row in result.fetchall():
            row_data = {}
            for column, value in zip(result.keys(), row):  # type: ignore
                row_data[column] = value
            results.append(row_data)

        return results

    def get_all(self, user_id):
        query_data = (
            self.__session.query(ProjectModel)
            .outerjoin(
                SprintModel,
                and_(
                    ProjectModel.id == SprintModel.project_id,
                    SprintModel.state == "IN PROGRESS",
                ),
            )
            .filter(
                or_(
                    ProjectModel.leader_id == user_id,
                    ProjectModel.product_owner_id == user_id,
                    ProjectModel.collaborators_ids.any(
                        ProjectCollaboratorModel.user_id == user_id
                    ),
                )
            )
            .all()
        )

        projects = []

        for row in query_data:
            project = ProjectSqlalchemyMapper.toListDomain(row)
            projects.append(project)

        return projects

    def get_by_id(self, id: UUID):
        project = (
            self.__session.query(ProjectModel).filter(ProjectModel.id == id).first()
        )

        if project is not None:
            return ProjectSqlalchemyMapper.toDomain(project)

        return None

    def delete(self, id: UUID):
        data = self.__session.get(ProjectModel, id)

        if data is not None:
            self.__session.delete(data)
            self.__session.commit()
        else:
            raise ResourceNotFoundException("Project")

    def add_tag_status(
        self,
        project_id,
        instance: TagModel | StatusModel,
        instance_name,
    ):
        project_instance = (
            self.__session.query(ProjectModel).filter_by(id=project_id).first()
        )

        if project_instance is None:
            raise ResourceNotFoundException("Project")

        if instance_name == "tags":
            project_instance.tags.add(instance)
        else:
            project_instance.status.add(instance)

        self.__session.commit()
        return "Sucessfully added"

    def partial_update(self, id, data):
        stmt = (
            update(ProjectModel)
            .where(ProjectModel.id == id)
            .values(**data)
            .returning(ProjectModel)
        )
        result = self.__session.execute(stmt)

        updated_data = result.fetchone()

        self.__session.commit()

        return ProjectSqlalchemyMapper.toDomain(updated_data[0])

    def add_collaborator(self, id, collaborator_id):
        project_collaborator = (
            self.__session.query(ProjectCollaboratorModel)
            .filter_by(project_id=id, user_id=collaborator_id)
            .first()
        )

        if project_collaborator is None:
            project_collaborator = ProjectCollaboratorModel(
                project_id=id, user_id=collaborator_id
            )

            try:
                self.__session.add(project_collaborator)
                self.__session.commit()
                return "Added"
            except Exception as e:
                raise ResourceNotFoundException(
                    e.args[0]
                    .split("is not present in table")[1]
                    .split('"')[1]
                    .capitalize()
                )

    def save(self, project_model):
        self.__session.commit()
        self.__session.refresh(project_model)
        return project_model

    def remove_tag(self, project_id, tag_instance):
        project_instance = self.__session.get(ProjectModel, project_id)

        project_instance.tags.remove(tag_instance)
        self.__session.commit()
        self.__session.refresh(project_instance)

        return project_instance

    def remove_status(self, project_id, status_instance):
        project_instance = self.__session.get(ProjectModel, project_id)

        project_instance.status.remove(status_instance)
        self.__session.commit()
        self.__session.refresh(project_instance)
        return project_instance
