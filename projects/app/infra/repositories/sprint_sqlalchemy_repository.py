from app.application.interfaces.repositories import SprintRepository
from app.domain.errors import ResourceNotFoundException
from app.infra.database.models import SprintModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


class SprintSqlalchemyRepository(SprintRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, data: dict):
        try:
            new_data = SprintModel(**data)

            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return new_data
        except IntegrityError as e:
            raise ResourceNotFoundException(
                e.args[0].split("is not present in table")[1].split('"')[1].capitalize()
            )

    # def get_all(self):
    #     data = self.__session.query(TaskModel).all()
    #     return data

    # def get_by_id(self, id: int):
    #     data = self.__session.query(TaskModel).get(id)
    #     return data

    # def partial_update(self, id: int, data):
    #     self.__session.query(TaskModel).filter(TaskModel.id == id).update(data)
    #     self.__session.commit()
    #     return "TODO"

    # def delete(self, id: int):
    #     data = self.__session.get(TaskModel, id)

    #     if data is not None:
    #         self.__session.delete(data)
    #         self.__session.commit()
    #         return True

    #     return False
