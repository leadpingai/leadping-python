from enum import Enum

class DispositionCategory(str, Enum):
    Open = "Open",
    Qualified = "Qualified",
    Converted = "Converted",
    Lost = "Lost",
    Invalid = "Invalid",
    Duplicate = "Duplicate",

