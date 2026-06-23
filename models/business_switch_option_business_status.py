from enum import Enum

class BusinessSwitchOption_businessStatus(str, Enum):
    SettingUp = "SettingUp",
    SetupCompleted = "SetupCompleted",
    Active = "Active",

