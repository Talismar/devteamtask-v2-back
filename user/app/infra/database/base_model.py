from enum import Enum
from typing import Literal
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Enum as SQLAlchemyEnum


class BaseModel(DeclarativeBase):
    type_annotation_map = {
        Enum: SQLAlchemyEnum(Enum),
        Literal: SQLAlchemyEnum(Enum),
    }
