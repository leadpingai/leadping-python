from enum import Enum

class OutboundDeliveryChannel(str, Enum):
    Sms = "sms",
    Voice = "voice",
    Email = "email",
    Webhook = "webhook",
    Internal_notification = "internal_notification",

