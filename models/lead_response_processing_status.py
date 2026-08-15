from enum import Enum

class LeadResponse_processingStatus(str, Enum):
    Verifying = "Verifying",
    Validating = "Validating",
    Enriching = "Enriching",
    Ready = "Ready",
    Invalid = "Invalid",
    Failed = "Failed",

