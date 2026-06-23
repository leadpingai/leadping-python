from enum import Enum

class ActivationOnboardingStatus(str, Enum):
    Draft = "Draft",
    Submitted = "Submitted",
    Failed = "Failed",

