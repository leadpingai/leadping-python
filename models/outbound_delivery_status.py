from enum import Enum

class OutboundDeliveryStatus(str, Enum):
    Pending = "pending",
    Scheduled = "scheduled",
    Reserved = "reserved",
    Sending = "sending",
    Sent = "sent",
    Failed = "failed",
    Skipped = "skipped",
    Blocked = "blocked",
    Cancelled = "cancelled",

