from enum import Enum

class SendSmsRequest_outboundPriority(str, Enum):
    Critical_internal_notification = "critical_internal_notification",
    Fresh_inbound_lead_response = "fresh_inbound_lead_response",
    Manual_user_initiated = "manual_user_initiated",
    Active_conversation_reply = "active_conversation_reply",
    Automation_follow_up = "automation_follow_up",
    Campaign_message = "campaign_message",
    Imported_lead_campaign = "imported_lead_campaign",
    Warmup = "warmup",
    Retry = "retry",

