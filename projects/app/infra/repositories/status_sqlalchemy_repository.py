from sqlalchemy import func
from sqlalchemy.orm import Session

from app.application.repositories import StatusRepository
from app.infra.database.models.status_model import StatusModel
from app.infra.repositories.mapper.status_sqlalchemy_mapper import (
    StatusSqlalchemyMapper,
)


class StatusSqlalchemyRepository(StatusRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_or_create(self, data: dict[str, str]):
        status_already_exists = (
            self.__session.query(StatusModel)
            .filter(func.lower(StatusModel.name) == data["name"].lower())
            .first()
        )
        if status_already_exists is not None:
            return status_already_exists
        else:
            new_data = StatusModel(**data)

            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return new_data

    def get_all(self):
        data = self.__session.query(StatusModel).all()
        return data

    def get_by_id(self, id: int):
        data = self.__session.get(StatusModel, id)
        return data

    def delete(self, id: int):
        data = self.__session.get(StatusModel, id)

        if data is not None:
            self.__session.delete(data)
            self.__session.commit()
            return True

        return False
