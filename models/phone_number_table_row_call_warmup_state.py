from enum import Enum

class PhoneNumberTableRow_callWarmupState(str, Enum):
    NotStarted = "Not Started",
    NotEligible = "Not Eligible",
    Warming = "Warming",
    Warmed = "Warmed",
    Paused = "Paused",
    NeedsAttention = "Needs Attention",
    Blocked = "Blocked",

