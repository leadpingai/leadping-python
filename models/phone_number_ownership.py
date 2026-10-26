from enum import Enum

class PhoneNumberOwnership(str, Enum):
    Unassigned = "Unassigned",
    Leadping = "Leadping",
    Organization = "Organization",

