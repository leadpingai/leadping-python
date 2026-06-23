from enum import Enum

class OutgoingNumberSelectionRequest_channel(str, Enum):
    Sms = "sms",
    Call = "call",

