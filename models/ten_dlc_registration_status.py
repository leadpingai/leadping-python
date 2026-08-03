from enum import Enum

class TenDlcRegistrationStatus(str, Enum):
    NotSubmitted = "NotSubmitted",
    Pending = "Pending",
    Approved = "Approved",
    Rejected = "Rejected",
    Failed = "Failed",

