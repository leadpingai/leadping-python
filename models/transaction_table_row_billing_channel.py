from enum import Enum

class TransactionTableRow_billingChannel(str, Enum):
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
    Connection = "connection",
    Automation = "automation",

