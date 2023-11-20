from app.infra.database.models import SprintModel, StatusModel
from app.infra.database.utils import attribute_names


def test_should_it_possible_to_return_attribute_names_of_sqlalchemy_models():
    attrs_names = attribute_names(SprintModel)

    assert "project_id" in attrs_names
    assert "name" in attrs_names
