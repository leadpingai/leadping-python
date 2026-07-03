from enum import Enum

class BusinessTableRow_status(str, Enum):
    SettingUp = "SettingUp",
    SetupCompleted = "SetupCompleted",
    Active = "Active",

