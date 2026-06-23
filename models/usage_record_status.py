from enum import Enum

class UsageRecordStatus(str, Enum):
    Recorded = "recorded",
    Rated = "rated",
    Pending_invoice = "pending_invoice",
    Invoiced = "invoiced",
    Charged = "charged",
    Failed = "failed",
    Refunded_credited = "refunded_credited",
    Non_billable_internal = "non_billable_internal",
    Blocked_due_to_billing = "blocked_due_to_billing",

