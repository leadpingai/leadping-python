from enum import Enum

class BusinessResponse_setupStatus(str, Enum):
    Personal = "Personal",
    Business = "Business",
    Details = "Details",
    Compliance = "Compliance",
    Phone = "Phone",
    Plan = "Plan",
    Billing = "Billing",
    Review = "Review",
    Complete = "Complete",

