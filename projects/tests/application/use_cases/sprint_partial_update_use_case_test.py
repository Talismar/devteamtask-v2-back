from app.application.use_cases import SprintPartialUpdateUseCase
from tests.base_classes import SprintBaseTest


class TestSprintPartialUpdateUseCase(SprintBaseTest):
    def test_partial_update(self):
        self.sut = SprintPartialUpdateUseCase(self.sprint_repository)

        project = self.make_project()
        project_id = project.data_created["id"]

        name_to_create = self.fake.name()
        description_to_create = self.fake.name()

        sprint_created = self.sprint_repository.create(
            {
                "name": name_to_create,
                "description": description_to_create,
                "project_id": project_id,
            },
        )

        name_to_update = self.fake.name()
        sprint_updated = self.sut.execute(
            sprint_created["id"], {"name": name_to_update}
        )

        assert sprint_updated["name"] == name_to_update
        assert sprint_updated["description"] == description_to_create
