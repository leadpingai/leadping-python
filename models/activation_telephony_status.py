from enum import Enum

class ActivationTelephonyStatus(str, Enum):
    NotStarted = "NotStarted",
    ProvisioningPending = "ProvisioningPending",
    PartiallyProvisioned = "PartiallyProvisioned",
    Ready = "Ready",
    Failed = "Failed",
    BlockedRequiresOperatorAction = "BlockedRequiresOperatorAction",

