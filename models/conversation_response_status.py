from enum import Enum

class ConversationResponse_status(str, Enum):
    Needs_reply = "needs_reply",
    Waiting = "waiting",
    Failed = "failed",
    Open = "open",

