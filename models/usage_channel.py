from enum import Enum

class UsageChannel(str, Enum):
    Lead = "lead",
    Sms = "sms",
    Mms = "mms",
    Email = "email",
    Voice = "voice",
    Phone_number = "phone_number",
    Warmup = "warmup",
    Website = "website",
    Openai = "openai",
    Domain = "domain",
    OneZerodlc = "10dlc",
    Payment = "payment",
    Connection = "connection",
    Automation = "automation",

