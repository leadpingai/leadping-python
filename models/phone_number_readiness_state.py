from enum import Enum

class PhoneNumberReadiness_state(str, Enum):
    NotStarted = "Not Started",
    InProgress = "In Progress",
    Paused = "Paused",
    Blocked = "Blocked",
    Ready = "Ready",

