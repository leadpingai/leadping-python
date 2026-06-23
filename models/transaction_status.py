from enum import Enum

class TransactionStatus(str, Enum):
    Pending = "Pending",
    Confirmed = "Confirmed",
    Failed = "Failed",

