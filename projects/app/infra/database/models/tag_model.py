from typing import Set

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..associations import ProjectTagModel
from ..base_model import BaseModel
from ..mixins import CommonMixin


class TagModel(CommonMixin, BaseModel):
    name: Mapped[str] = mapped_column(String(48))
    projects: Mapped[Set["ProjectModel"]] = relationship(
        secondary=ProjectTagModel, back_populates="tags"
    )
