from enum import Enum

class FeedbackAdminUpdateRequest_status(str, Enum):
    New = "new",
    Reviewed = "reviewed",
    Planned = "planned",
    In_progress = "in_progress",
    Shipped = "shipped",
    Closed = "closed",
    Ignored = "ignored",

