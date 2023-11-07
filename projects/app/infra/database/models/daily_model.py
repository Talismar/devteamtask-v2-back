from typing import Optional

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base_model import BaseModel
from ..mixins import CommonMixin, TimestampMixin


class DailyModel(CommonMixin, TimestampMixin, BaseModel):
    note: Mapped[Optional[str]] = mapped_column(Text())
    event_notes_id: Mapped[int] = mapped_column(
        ForeignKey(column="eventnotes.id", ondelete="CASCADE")
    )
    event_notes: Mapped["EventNotesModel"] = relationship(back_populates="daily")
