from enum import Enum

class BusinessResponse_subscriptionStatus(str, Enum):
    Pending = "Pending",
    Active = "Active",
    Overdue = "Overdue",
    Canceled = "Canceled",

