from enum import Enum

class LeadStatusChangeExportRow_changeSource(str, Enum):
    User = "User",
    AI = "AI",
    Automation = "Automation",
    System = "System",
    API = "API",

