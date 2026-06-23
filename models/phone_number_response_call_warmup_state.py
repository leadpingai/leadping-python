from enum import Enum

class PhoneNumberResponse_callWarmupState(str, Enum):
    NotStarted = "Not Started",
    NotEligible = "Not Eligible",
    Warming = "Warming",
    Warmed = "Warmed",
    Paused = "Paused",
    NeedsAttention = "Needs Attention",
    Blocked = "Blocked",

