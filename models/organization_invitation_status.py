from enum import Enum

class OrganizationInvitationStatus(str, Enum):
    AwaitingWorkOSConfirmation = "Awaiting WorkOS confirmation",
    Pending = "Pending",
    Accepted = "Accepted",
    Expired = "Expired",
    Revoked = "Revoked",
    Resent = "Resent",
    FailedToSend = "Failed to send",

