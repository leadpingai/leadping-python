from enum import Enum

class EventDetailResponse_status(str, Enum):
    Pending = "Pending",
    InProgress = "InProgress",
    Completed = "Completed",
    Failed = "Failed",
    Cancelled = "Cancelled",

