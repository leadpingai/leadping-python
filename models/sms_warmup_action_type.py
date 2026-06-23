from enum import Enum

class SmsWarmupActionType(str, Enum):
    OutboundMessage = "OutboundMessage",
    ReplyMessage = "ReplyMessage",
    HealthCheck = "HealthCheck",
    Audit = "Audit",

