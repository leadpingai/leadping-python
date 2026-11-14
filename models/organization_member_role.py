from enum import Enum

class OrganizationMemberRole(str, Enum):
    AccountAdmin = "Account Admin",
    Owner = "Owner",
    Admin = "Admin",
    Agent = "Agent",

