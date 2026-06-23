from enum import Enum

class CurrentDispositionSummary_source(str, Enum):
    User = "User",
    AI = "AI",
    Automation = "Automation",
    System = "System",
    API = "API",

