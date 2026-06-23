from enum import Enum

class EventTimelineType(str, Enum):
    Message = "Message",
    Sms = "Sms",
    Mms = "Mms",
    Call = "Call",
    Voicemail = "Voicemail",
    Note = "Note",
    Disposition = "Disposition",
    LeadCreated = "LeadCreated",
    LeadUpdated = "LeadUpdated",
    Notification = "Notification",
    Payment = "Payment",
    Warmup = "Warmup",

