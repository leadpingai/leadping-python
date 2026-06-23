from enum import Enum

class PhoneNumberWarmupCallStatus(str, Enum):
    Created = "Created",
    Scheduled = "Scheduled",
    Placing = "Placing",
    Ringing = "Ringing",
    Answered = "Answered",
    Connected = "Connected",
    Completed = "Completed",
    Failed = "Failed",
    Canceled = "Canceled",
    Skipped = "Skipped",
    TimedOut = "TimedOut",

