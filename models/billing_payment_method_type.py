from enum import Enum

class BillingPaymentMethodType(str, Enum):
    Card = "card",
    Link = "link",

