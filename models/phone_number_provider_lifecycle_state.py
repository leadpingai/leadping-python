from enum import Enum

class PhoneNumberProviderLifecycleState(str, Enum):
    Unknown = "Unknown",
    Requested = "Requested",
    Purchasing = "Purchasing",
    Purchased = "Purchased",
    Provisioning = "Provisioning",
    Active = "Active",
    Failed = "Failed",
    Released = "Released",
    Suspended = "Suspended",

