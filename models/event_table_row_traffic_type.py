from enum import Enum

class EventTableRow_trafficType(str, Enum):
    RealLead = "RealLead",
    Warmup = "Warmup",
    Test = "Test",
    SystemInternal = "SystemInternal",
    FailedAttempt = "FailedAttempt",

