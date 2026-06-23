from enum import Enum

class ActivationPaymentStatus(str, Enum):
    PaymentMethodPending = "PaymentMethodPending",
    PaymentMethodConfirmed = "PaymentMethodConfirmed",
    Failed = "Failed",

