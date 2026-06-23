from enum import Enum

class PhoneNumberResponse_healthStatus(str, Enum):
    NotStarted = "Not Started",
    Warming = "Warming",
    Healthy = "Healthy",
    NeedsAttention = "Needs Attention",
    Paused = "Paused",
    Blocked = "Blocked",
    Ready = "Ready",

