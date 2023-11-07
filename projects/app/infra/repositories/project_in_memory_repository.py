from app.application.interfaces.repositories import ProjectRepository


class ProjectInMemoryRepository(ProjectRepository):
    def __init__(self) -> None:
        self.data = []

    def create(self, data):
        self.data.append(data)
        return
