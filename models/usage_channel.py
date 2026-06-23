from enum import Enum

class UsageChannel(str, Enum):
    Sms = "sms",
    Mms = "mms",
    Email = "email",
    Voice = "voice",
    Phone_number = "phone_number",
    Warmup = "warmup",
    Website = "website",
    Domain = "domain",
    OneZerodlc = "10dlc",
    Connection = "connection",
    Automation = "automation",

