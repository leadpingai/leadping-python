from enum import Enum

class PhoneNumberReadiness_healthStatus(str, Enum):
    NotEvaluated = "Not Evaluated",
    Evaluating = "Evaluating",
    Healthy = "Healthy",
    NeedsAttention = "Needs Attention",
    Blocked = "Blocked",

