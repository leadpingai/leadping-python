from enum import Enum

class OrganizationResponse_setupStatus(str, Enum):
    Personal = "Personal",
    Organization = "Organization",
    Details = "Details",
    Compliance = "Compliance",
    Phone = "Phone",
    Plan = "Plan",
    Billing = "Billing",
    Review = "Review",
    Complete = "Complete",

