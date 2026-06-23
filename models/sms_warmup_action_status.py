from enum import Enum

class SmsWarmupActionStatus(str, Enum):
    Scheduled = "Scheduled",
    Sending = "Sending",
    Sent = "Sent",
    Delivered = "Delivered",
    Received = "Received",
    Failed = "Failed",
    Skipped = "Skipped",
    Paused = "Paused",
    Blocked = "Blocked",
    Cancelled = "Cancelled",

