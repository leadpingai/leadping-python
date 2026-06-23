from enum import Enum

class UserResponse_subscriptionStatus(str, Enum):
    Pending = "Pending",
    Active = "Active",
    Overdue = "Overdue",
    Canceled = "Canceled",

