from enum import Enum

class PhoneIdentityLookupActionType(str, Enum):
    Validation = "validation",
    Enrichment = "enrichment",
    UnwantedNumberCheck = "unwanted-number-check",

