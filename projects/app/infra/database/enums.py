from enum import Enum


class StateEnum(str, Enum):
    IN_PROGRESS = "IN PROGRESS"
    COMPLETED = "COMPLETED"


class DefaultStatusEnum(str, Enum):
    TO_DO = "TO DO"
    DOING = "DOING"
    DONE = "DONE"
