from enum import Enum

class PhoneNumberResponse_warmupState(str, Enum):
    NotStarted = "Not Started",
    Warming = "Warming",
    Healthy = "Healthy",
    NeedsAttention = "Needs Attention",
    Paused = "Paused",
    Blocked = "Blocked",
    Ready = "Ready",

