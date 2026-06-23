from enum import Enum

class DispositionRequest_category(str, Enum):
    Open = "Open",
    Qualified = "Qualified",
    Converted = "Converted",
    Lost = "Lost",
    Invalid = "Invalid",
    Duplicate = "Duplicate",

