from enum import Enum

class CallEventTableRow_status(str, Enum):
    Scheduled = "scheduled",
    Queued = "queued",
    Initiated = "initiated",
    Ringing = "ringing",
    In_progress = "in_progress",
    Active = "active",
    Completed = "completed",
    Ended = "ended",
    Busy = "busy",
    No_answer = "no_answer",
    Failed = "failed",
    Canceled = "canceled",
    Missed = "missed",
    Transferred = "transferred",
    Voicemail = "voicemail",
    Blocked_billing = "blocked_billing",
    Blocked_phone_number_status = "blocked_phone_number_status",
    Blocked_configuration = "blocked_configuration",
    Blocked_permission = "blocked_permission",
    Configuration_required = "configuration_required",

