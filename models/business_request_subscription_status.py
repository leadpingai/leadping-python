from enum import Enum

class BusinessRequest_subscriptionStatus(str, Enum):
    Pending = "Pending",
    Active = "Active",
    Overdue = "Overdue",
    Canceled = "Canceled",

