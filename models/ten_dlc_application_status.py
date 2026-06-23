from enum import Enum

class TenDlcApplicationStatus(str, Enum):
    NotStarted = "NotStarted",
    DraftGenerated = "DraftGenerated",
    DraftNeedsAdminReview = "DraftNeedsAdminReview",
    ReadyToSubmit = "ReadyToSubmit",
    Submitted = "Submitted",
    PendingTelnyxReview = "PendingTelnyxReview",
    Approved = "Approved",
    Rejected = "Rejected",
    NeedsChanges = "NeedsChanges",
    ResubmissionReady = "ResubmissionReady",
    Failed = "Failed",

