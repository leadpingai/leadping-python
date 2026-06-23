from enum import Enum

class ActivationSubscriptionStatus(str, Enum):
    Pending = "Pending",
    Active = "Active",
    Failed = "Failed",
    Canceled = "Canceled",

