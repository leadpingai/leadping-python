from enum import Enum

class InitiateCallRequest_selectionReason(str, Enum):
    StickyConversation = "StickyConversation",
    LeadAssigned = "LeadAssigned",
    CampaignOrSource = "CampaignOrSource",
    Preferred = "Preferred",
    LocalArea = "LocalArea",
    HealthyPool = "HealthyPool",
    FallbackDefault = "FallbackDefault",
    ManualOverride = "ManualOverride",

