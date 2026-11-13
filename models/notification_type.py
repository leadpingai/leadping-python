from enum import Enum

class NotificationType(str, Enum):
    Appointment = "Appointment",
    General = "General",
    Lead = "Lead",
    Call = "Call",
    Sms = "Sms",
    Billing = "Billing",
    System = "System",
    Success = "Success",
    Warning = "Warning",
    Error = "Error",
    Info = "Info",
    Announcement = "Announcement",
    Activation = "Activation",

