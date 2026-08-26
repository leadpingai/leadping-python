from enum import Enum

class LeadTableRow_processingStatus(str, Enum):
    Quarantined = "Quarantined",
    Verifying = "Verifying",
    Validating = "Validating",
    Enriching = "Enriching",
    Ready = "Ready",
    Invalid = "Invalid",
    Failed = "Failed",

