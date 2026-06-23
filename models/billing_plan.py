from enum import Enum

class BillingPlan(str, Enum):
    Annual = "Annual",
    Monthly = "Monthly",

