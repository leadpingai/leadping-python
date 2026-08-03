from enum import Enum

class BillableUnit(str, Enum):
    Lead_received = "lead_received",
    Phone_identity_lookup = "phone_identity_lookup",
    Sms_segment = "sms_segment",
    Mms_message = "mms_message",
    Email_message = "email_message",
    Voice_minute = "voice_minute",
    Phone_number_month = "phone_number_month",
    Warmup_sms_segment = "warmup_sms_segment",
    Warmup_voice_minute = "warmup_voice_minute",
    Website_setup = "website_setup",
    Openai_operation = "openai_operation",
    Domain_registration = "domain_registration",
    OneZerodlc_application = "10dlc_application",
    Connection_action = "connection_action",
    Automation_run = "automation_run",

