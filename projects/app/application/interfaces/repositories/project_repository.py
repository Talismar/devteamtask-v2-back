from abc import ABC, abstractmethod
from typing import TypedDict
from uuid import UUID


class PartialUpdateRequestDataTypes(TypedDict):
    name: None | str
    end_date: None | str
    product_owner: None | str


class ProjectRepository(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id: UUID):
        pass

    @abstractmethod
    def add_tag(self, project_id: UUID, tag_instance):
        pass

    @abstractmethod
    def partial_update(self, project_model, data: PartialUpdateRequestDataTypes):
        pass

    @abstractmethod
    def save(self, project_model):
        pass
