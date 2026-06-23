from enum import Enum

class WalletResponse_sourceType(str, Enum):
    Purchase = "purchase",
    Promo = "promo",
    Admin_adjustment = "admin_adjustment",
    Refund_adjustment = "refund_adjustment",
    Migration = "migration",
    Chargeback_reversal = "chargeback_reversal",
    Compromise_restoration = "compromise_restoration",

