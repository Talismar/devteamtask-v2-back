from typing import Optional, Set

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base_model import BaseModel
from ..mixins import CommonMixin


class EventNotesModel(CommonMixin, BaseModel):
    planning: Mapped[Optional[str]] = mapped_column(Text())
    review: Mapped[Optional[str]] = mapped_column(Text())
    retrospective: Mapped[Optional[str]] = mapped_column(Text())

    sprint_id: Mapped[int] = mapped_column(
        ForeignKey(column="sprint.id", ondelete="CASCADE")
    )
    sprint: Mapped["SprintModel"] = relationship(back_populates="event_notes")

    daily: Mapped[Set["DailyModel"]] = relationship(back_populates="event_notes")
