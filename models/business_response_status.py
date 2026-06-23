from enum import Enum

class BusinessResponse_status(str, Enum):
    SettingUp = "SettingUp",
    SetupCompleted = "SetupCompleted",
    Active = "Active",

