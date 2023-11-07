from uuid import UUID

from app.application.interfaces.repositories import ProjectRepository
from app.domain.errors import ResourceNotFoundException
from app.infra.database.models import ProjectCollaboratorModel, ProjectModel, TagModel
from app.infra.database.utils import attribute_names
from sqlalchemy import or_, text
from sqlalchemy.orm import Session


class ProjectSqlalchemyRepository(ProjectRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, data):
        new_data = ProjectModel(**data)
        self.__session.add(new_data)
        self.__session.commit()
        self.__session.refresh(new_data)

        return new_data

    def get_users_data(self, data: list[ProjectModel]):
        leaders_ids = [row.leader_id for row in data]
        product_owners_ids = []
        collaborators_ids = []

        for row in data:
            if row.product_owner_id is None:
                continue
            product_owners_ids.append(row.product_owner_id)

        for project_row in data:
            if len(project_row.collaborators_ids) == 0:
                continue
            for collaborator_row in project_row.collaborators_ids:
                collaborators_ids.append(collaborator_row.user_id)

        users_ids = tuple(set(leaders_ids + product_owners_ids + collaborators_ids))

        params = {"users_ids": users_ids}
        query = "SELECT id, name, avatar_url FROM users WHERE id IN :users_ids;"
        result = self.__session.execute(text(query), params)
        results = []

        for row in result.fetchall():
            row_data = {}
            for column, value in zip(result.keys(), row):
                row_data[column] = value
            results.append(row_data)

        return results

    def get_all(self, user_id: int):
        data = (
            self.__session.query(ProjectModel)
            .filter(
                or_(
                    ProjectModel.leader_id == user_id,
                    ProjectModel.product_owner_id == user_id,
                    ProjectModel.collaborators_ids.any(
                        ProjectCollaboratorModel.user_id.in_([user_id])
                    ),
                )
            )
            .all()
        )

        users = self.get_users_data(data)

        return {"projects": data, "users": users}

    def get_by_id(self, id: UUID):
        data = self.__session.query(ProjectModel).get(id)

        if data is not None:
            users = self.get_users_data([data])
            return {
                "project_data": {
                    "id": data.id,
                    "name": data.name,
                    "state": data.state,
                    "end_date": data.end_date,
                    "start_date": data.start_date,
                    "logo_url": data.logo_url,
                    "leader_id": data.leader_id,
                    "product_owner_id": data.product_owner_id,
                    "collaborators_ids": data.collaborators_ids,
                    "status": data.status,
                    "tags": data.tags,
                    "tasks": data.tasks,
                    "sprints": data.sprints,
                },
                "users": users,
            }

        return data

    def add_tag(self, project_id: UUID, tag_instance: TagModel):
        project_instance = (
            self.__session.query(ProjectModel).filter_by(id=project_id).first()
        )

        if project_instance is None:
            raise ResourceNotFoundException("Project")

        project_instance.tags.add(tag_instance)
        self.__session.commit()
        return "Sucessfully added"

    def partial_update(self, project_model: ProjectModel, data):
        for field, value in data.items():
            setattr(project_model, field, value)

        self.__session.commit()
        self.__session.refresh(project_model)
        return project_model

    def save(self, project_model):
        self.__session.commit()
        self.__session.refresh(project_model)
        return project_model
