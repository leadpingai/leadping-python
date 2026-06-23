from enum import Enum

class PhoneNumberOutboundHealthStatus(str, Enum):
    Unknown = "unknown",
    New = "new",
    Healthy = "healthy",
    Warmup = "warmup",
    Limited = "limited",
    Cooling_down = "cooling_down",
    Suspended = "suspended",
    Disabled = "disabled",

