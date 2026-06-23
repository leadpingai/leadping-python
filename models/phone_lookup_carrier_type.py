from enum import Enum

class PhoneLookup_carrierType(str, Enum):
    FixedLine = "FixedLine",
    Mobile = "Mobile",
    Voip = "Voip",
    FixedLineOrMobile = "FixedLineOrMobile",
    TollFree = "TollFree",
    PremiumRate = "PremiumRate",
    SharedCost = "SharedCost",
    PersonalNumber = "PersonalNumber",
    Pager = "Pager",
    Uan = "Uan",
    Voicemail = "Voicemail",
    Unknown = "Unknown",

