from app.application.interfaces.repositories import TagRepository
from app.infra.database.models.tag_model import TagModel
from sqlalchemy import func
from sqlalchemy.orm import Session


class TagSqlalchemyRepository(TagRepository):
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_or_create(self, data: dict[str, str]):
        tag_already_exists = (
            self.__session.query(TagModel)
            .filter(func.lower(TagModel.name) == data["name"].lower())
            .first()
        )
        if tag_already_exists:
            return tag_already_exists
        else:
            new_data = TagModel(**data)
            self.__session.add(new_data)
            self.__session.commit()
            self.__session.refresh(new_data)

            return new_data

    def get_all(self):
        data = self.__session.query(TagModel).all()
        return data

    def get_by_id(self, id: int):
        data = self.__session.query(TagModel).get(id)
        return data

    def delete(self, id: int):
        data = self.__session.get(TagModel, id)
        if data:
            self.__session.delete(data)
            self.__session.commit()
