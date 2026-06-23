from enum import Enum

class SmsEventTableRow_outboundSource(str, Enum):
    Manual = "manual",
    Automation = "automation",
    Campaign = "campaign",
    Import_ = "import",
    Api = "api",
    System_notification = "system_notification",
    Warmup = "warmup",
    Retry = "retry",

