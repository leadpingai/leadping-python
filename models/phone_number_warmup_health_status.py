from enum import Enum

class PhoneNumberWarmupHealthStatus(str, Enum):
    NotStarted = "Not Started",
    NotEligible = "Not Eligible",
    Warming = "Warming",
    Warmed = "Warmed",
    Paused = "Paused",
    NeedsAttention = "Needs Attention",
    Blocked = "Blocked",

