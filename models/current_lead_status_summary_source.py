from enum import Enum

class CurrentLeadStatusSummary_source(str, Enum):
    User = "User",
    AI = "AI",
    Automation = "Automation",
    System = "System",
    API = "API",

