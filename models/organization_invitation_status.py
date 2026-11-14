from enum import Enum

class OrganizationInvitationStatus(str, Enum):
    Declined = "Declined",
    AwaitingConfirmation = "Awaiting confirmation",
    Pending = "Pending",
    Accepted = "Accepted",
    Expired = "Expired",
    Revoked = "Revoked",
    Resent = "Resent",
    FailedToSend = "Failed to send",

