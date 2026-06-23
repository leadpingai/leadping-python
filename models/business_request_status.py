from enum import Enum

class BusinessRequest_status(str, Enum):
    SettingUp = "SettingUp",
    SetupCompleted = "SetupCompleted",
    Active = "Active",

