from enum import Enum

class FeedbackStatus(str, Enum):
    New = "new",
    Reviewed = "reviewed",
    Planned = "planned",
    In_progress = "in_progress",
    Shipped = "shipped",
    Closed = "closed",
    Ignored = "ignored",

