from enum import Enum

class BusinessSwitchOption_tenDlcStatus(str, Enum):
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

