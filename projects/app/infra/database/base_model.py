from enum import Enum
from typing import Literal

from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.orm import DeclarativeBase, declared_attr


class BaseModel(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()[:-5]

    type_annotation_map = {
        Enum: SQLAlchemyEnum(Enum),
        Literal: SQLAlchemyEnum(Enum),
    }
