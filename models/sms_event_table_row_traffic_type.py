from enum import Enum

class SmsEventTableRow_trafficType(str, Enum):
    RealLead = "RealLead",
    Warmup = "Warmup",
    Test = "Test",
    SystemInternal = "SystemInternal",
    FailedAttempt = "FailedAttempt",

