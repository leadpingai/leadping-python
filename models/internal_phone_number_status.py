from enum import Enum

class InternalPhoneNumberStatus(str, Enum):
    Unregistered = "Unregistered",
    Provisioning = "Provisioning",
    FailedProvisioning = "FailedProvisioning",
    Active = "Active",
    Expired = "Expired",
    Suspended = "Suspended",
    PendingRelease = "PendingRelease",

