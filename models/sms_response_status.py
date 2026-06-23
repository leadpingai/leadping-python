from enum import Enum

class SmsResponse_status(str, Enum):
    Draft = "draft",
    Scheduled = "scheduled",
    Queued = "queued",
    Sending = "sending",
    Sent = "sent",
    Received = "received",
    Delivered = "delivered",
    Failed = "failed",
    Undeliverable = "undeliverable",
    Opted_out = "opted_out",
    Blocked_compliance = "blocked_compliance",
    Blocked_billing = "blocked_billing",
    Blocked_missing_campaign = "blocked_missing_campaign",
    Canceled = "canceled",

