from enum import Enum

class UserDataExportStatuses(str, Enum):
    Pending = "Pending",
    Processing = "Processing",
    Completed = "Completed",
    Failed = "Failed",
    Expired = "Expired",

