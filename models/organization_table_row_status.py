from enum import Enum

class OrganizationTableRow_status(str, Enum):
    SettingUp = "SettingUp",
    SetupCompleted = "SetupCompleted",
    Active = "Active",

