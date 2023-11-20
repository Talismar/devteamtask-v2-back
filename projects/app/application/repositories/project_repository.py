from abc import ABC, abstractmethod
from typing import Literal, TypedDict
from uuid import UUID

from app.domain.entities.project import Project


class PartialUpdateRequestDataTypes(TypedDict, total=False):
    name: str
    end_date: str
    product_owner_id: int
    collaborator_id: int


class ProjectGetByIdReturnTypes(TypedDict, total=False):
    project_data: Project


class ProjectRepository(ABC):
    @abstractmethod
    def create(self, data: Project) -> Project:
        pass

    @abstractmethod
    def get_all(self, user_id: int):
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Project | None:
        pass

    @abstractmethod
    def delete(self, id: UUID):
        pass

    @abstractmethod
    def add_tag_status(
        self, project_id: UUID, instance, instance_name: Literal["tags", "status"]
    ):
        pass

    @abstractmethod
    def partial_update(
        self, id: UUID, data: PartialUpdateRequestDataTypes
    ) -> Project | None:
        pass

    @abstractmethod
    def add_collaborator(self, id: UUID, collaborator_id: int):
        pass

    @abstractmethod
    def get_users_data(self, users_ids: tuple[int]):
        pass

    @abstractmethod
    def save(self, project_model):
        pass
