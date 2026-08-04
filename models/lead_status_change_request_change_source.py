from enum import Enum

class LeadStatusChangeRequest_changeSource(str, Enum):
    User = "User",
    AI = "AI",
    Automation = "Automation",
    System = "System",
    API = "API",

