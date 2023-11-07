from datetime import datetime
from typing import List

from .status import Status


class Project:
    def __init__(
        self, id, name, start_date: datetime, end_date: datetime, status: List[Status]
    ) -> None:
        self.__id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
