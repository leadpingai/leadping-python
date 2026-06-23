from enum import Enum

class NotificationPriority(str, Enum):
    Low = "Low",
    Medium = "Medium",
    High = "High",
    Critical = "Critical",

