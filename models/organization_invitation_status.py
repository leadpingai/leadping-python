from enum import Enum

class OrganizationInvitationStatus(str, Enum):
    Pending = "Pending",
    Accepted = "Accepted",
    Expired = "Expired",
    Revoked = "Revoked",
    Resent = "Resent",
    FailedToSend = "Failed to send",

