from enum import Enum

class BusinessUserRole(str, Enum):
    Owner = "Owner",
    Admin = "Admin",
    Agent = "Agent",

