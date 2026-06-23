from enum import Enum

class WalletResponse_creditStatus(str, Enum):
    Active = "active",
    Consumed = "consumed",
    Expired = "expired",
    Refunded = "refunded",
    Voided = "voided",
    Disputed = "disputed",

