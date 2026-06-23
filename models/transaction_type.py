from enum import Enum

class TransactionType(str, Enum):
    Debit = "Debit",
    Adjustment = "Adjustment",
    Deposit = "Deposit",

