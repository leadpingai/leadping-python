from enum import Enum

class ActivationLaunchReviewStatus(str, Enum):
    NotReady = "NotReady",
    Pending = "Pending",
    Approved = "Approved",
    NotRequired = "NotRequired",
    Blocked = "Blocked",

