from enum import Enum

class SmsResponse_trafficType(str, Enum):
    RealLead = "RealLead",
    Warmup = "Warmup",
    Test = "Test",
    SystemInternal = "SystemInternal",
    FailedAttempt = "FailedAttempt",

