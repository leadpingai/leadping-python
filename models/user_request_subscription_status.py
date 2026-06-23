from enum import Enum

class UserRequest_subscriptionStatus(str, Enum):
    Pending = "Pending",
    Active = "Active",
    Overdue = "Overdue",
    Canceled = "Canceled",

