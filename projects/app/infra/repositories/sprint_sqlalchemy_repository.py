from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.application.repositories import SprintRepository
from app.domain.errors import ResourceNotFoundException
from app.infra.database.models import SprintModel

from .mapper.sprint_sqlalchemy_mapper import SprintSqlalchemyMapper


class SprintSqlalchemyRepository(SprintRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, data):
        try:
            new_data = SprintModel(**data)

            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return SprintSqlalchemyMapper.toDomain(new_data)
        except IntegrityError as e:
            raise ResourceNotFoundException(
                e.args[0].split("is not present in table")[1].split('"')[1].capitalize()
            )

    def partial_update(self, id, data):
        sprint_model = self.__session.get(SprintModel, id)

        if sprint_model is None:
            raise ResourceNotFoundException("Sprint")

        for key, value in data.items():
            setattr(sprint_model, key, value)

        self.__session.commit()
        self.__session.refresh(sprint_model)

        return SprintSqlalchemyMapper.toDomain(sprint_model)
