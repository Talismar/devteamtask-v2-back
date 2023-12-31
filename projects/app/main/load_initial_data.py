from app.infra.database.configuration import Session
from app.infra.database.models import ProjectModel, StatusModel


def create_status_initial():
    with Session() as session:
        session.begin()
        try:
            status_to_do = StatusModel(name="To Do")
            status_doing = StatusModel(name="Doing")
            status_done = StatusModel(name="Done")
            session.add_all([status_to_do, status_doing, status_done])
        except:
            session.rollback()
            raise
        else:
            session.commit()


def create_initial_project():
    with Session() as session:
        session.begin()
        try:
            data = {
                "name": "Project one",
                "start_date": "2023-10-29T19:37:39.931Z",
                "end_date": "2023-10-29T19:37:39.931Z",
                "leader_id": 1,
                # "collaborators_ids": [],
            }
            # project = ProjectModel(**data)
            # project_collaborators = ProjectCollaboratorModel(project_id=)
            # project.collaborators_ids.add()
            # session.add(project)
        except:
            session.rollback()
            raise
        else:
            session.commit()
