from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..base_model import BaseModel
from ..mixins import CommonMixin


class Invite(CommonMixin, BaseModel):
    email: Mapped[str]
    # project_id = ForeignKey(Project, on_delete=CASCADE)
    # expires = DateTimeField(default=in_three_days)
    # user_group = ForeignKey(Group, on_delete=PROTECT, related_name="user_group")
    # token = CharField(max_length=24, default=get_url)

    def __str__(self):
        return self.email
