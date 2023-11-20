from app.application.repositories import ProjectRepository
from app.domain.entities.project import Project


class ProjectInMemoryRepository(ProjectRepository):
    def __init__(self) -> None:
        self.data: list[Project] = []

    def create(self, data):
        self.data.append(data)
        return data

    def get_by_id(self, id):
        pass

    def delete(self, id):
        pass

    def add_tag(self, project_id, tag_instance):
        pass

    def partial_update(self, id, data):
        pass

    def add_collaborator(self, id, collaborator_id):
        pass

    def save(self, project_model):
        pass
