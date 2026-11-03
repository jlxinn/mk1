from enum import StrEnum, auto


class OrderStatusEnum(StrEnum):
    NEW = auto()
    SENT = auto()
    FAILED = auto()