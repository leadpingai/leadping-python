from enum import Enum

class SmsReadinessHealthStatus(str, Enum):
    NotEvaluated = "Not Evaluated",
    Evaluating = "Evaluating",
    Healthy = "Healthy",
    NeedsAttention = "Needs Attention",
    Blocked = "Blocked",

