from enum import Enum

class PhoneNumberInventoryState(str, Enum):
    Available = "Available",
    Assigned = "Assigned",
    PendingVerification = "Pending verification",
    ReadyForSMS = "Ready for SMS",
    ReadyForVoice = "Ready for voice",
    Restricted = "Restricted",
    Suspended = "Suspended",
    Failed = "Failed",
    Released = "Released",
    PendingRelease = "Pending release",
    WarmupOnly = "Warmup-only",
    InternalTestOnly = "Internal/test-only",

