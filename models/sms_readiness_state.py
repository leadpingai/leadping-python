from enum import Enum

class SmsReadinessState(str, Enum):
    NotStarted = "Not Started",
    InProgress = "In Progress",
    Paused = "Paused",
    Blocked = "Blocked",
    Ready = "Ready",

