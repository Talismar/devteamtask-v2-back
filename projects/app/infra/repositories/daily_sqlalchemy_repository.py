from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.application.repositories import DailyRepository
from app.domain.errors import ResourceNotFoundException
from app.infra.database.models import DailyModel, SprintModel

from .mapper.daily_sqlalchemy_mapper import DailySqlalchemyMapper


class DailySqlalchemyRepository(DailyRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, sprint_id, data):
        sprint_model = self.__session.get(SprintModel, sprint_id)

        if sprint_model is None:
            raise ResourceNotFoundException("Sprint")

        try:
            data.update({"event_notes_id": sprint_model.event_notes.id})
            new_data = DailyModel(**data)

            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return DailySqlalchemyMapper.toDomain(new_data)
        except IntegrityError:
            raise ResourceNotFoundException("Event Notes")

    def partial_update(self, id, data):
        daily_model = self.__session.get(DailyModel, id)

        if daily_model is None:
            raise ResourceNotFoundException("Daily")

        for key, value in data.items():
            setattr(daily_model, key, value)

        self.__session.commit()
        self.__session.refresh(daily_model)

        return DailySqlalchemyMapper.toDomain(daily_model)

    def get_by_id(self, id: int):
        daily_model = self.__session.get(DailyModel, id)

        if daily_model is None:
            raise ResourceNotFoundException("Daily")

        return DailySqlalchemyMapper.toDomain(daily_model)

    def get_all_by_sprint_id(self, sprint_id):
        sprint_model = self.__session.get(SprintModel, sprint_id)

        if sprint_model is None:
            raise ResourceNotFoundException("Sprint")

        if sprint_model.event_notes is None:
            return []

        return [
            DailySqlalchemyMapper.toDomain(daily)
            for daily in sprint_model.event_notes.daily
        ]
