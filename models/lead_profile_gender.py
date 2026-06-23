from enum import Enum

class LeadProfile_gender(str, Enum):
    M = "M",
    F = "F",
    NonBinary = "NonBinary",
    PreferNotToSay = "PreferNotToSay",
    Other = "Other",

