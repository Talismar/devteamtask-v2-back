from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.application.repositories import EventNotesRepository
from app.domain.errors import ResourceNotFoundException
from app.infra.database.models import EventNotesModel, SprintModel

from .mapper.event_notes_sqlalchemy_mapper import EventNotesSqlalchemyMapper


class EventNotesSqlalchemyRepository(EventNotesRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, data):
        try:
            new_data = EventNotesModel(**data)

            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return EventNotesSqlalchemyMapper.toDomain(new_data)
        except IntegrityError as e:
            raise ResourceNotFoundException(
                e.args[0].split("is not present in table")[1].split('"')[1].capitalize()
            )

    def partial_update(self, id, data):
        sprint_model = self.__session.get(EventNotesModel, id)

        if sprint_model is None:
            raise ResourceNotFoundException("Event Notes")

        for key, value in data.items():
            setattr(sprint_model, key, value)

        self.__session.commit()
        self.__session.refresh(sprint_model)

        return EventNotesSqlalchemyMapper.toDomain(sprint_model)

    def get_by_sprint_id(self, sprint_id):
        sprint_model = self.__session.get(SprintModel, sprint_id)

        if sprint_model is None:
            raise ResourceNotFoundException("Sprint")

        return EventNotesSqlalchemyMapper.toDomain(sprint_model.event_notes)
