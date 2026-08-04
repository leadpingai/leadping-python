from enum import Enum

class LeadStatusChangeExportRow_category(str, Enum):
    Open = "Open",
    Qualified = "Qualified",
    Converted = "Converted",
    Lost = "Lost",
    Invalid = "Invalid",
    Duplicate = "Duplicate",

