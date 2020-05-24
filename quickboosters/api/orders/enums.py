from enum import Enum


class StatusEnum(Enum):
    not_started = 1
    in_progress = 2
    complete = 3


class TypeEnum(Enum):
    solo_boost = 1
    duo_boost = 2
