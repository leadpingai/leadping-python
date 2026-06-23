from enum import Enum

class PhoneLookup_lineType(str, Enum):
    Wireline = "Wireline",
    Wireless = "Wireless",
    VoWiFi = "VoWiFi",
    VoIP = "VoIP",
    PrePaidWireless = "PrePaidWireless",
    Unknown = "Unknown",

