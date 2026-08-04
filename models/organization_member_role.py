from enum import Enum

class OrganizationMemberRole(str, Enum):
    Owner = "Owner",
    Admin = "Admin",
    Agent = "Agent",

