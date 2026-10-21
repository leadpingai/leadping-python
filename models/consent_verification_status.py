from enum import Enum

class ConsentVerificationStatus(str, Enum):
    Verified = "Verified",
    Unverified = "Unverified",
    Quarantined = "Quarantined",

