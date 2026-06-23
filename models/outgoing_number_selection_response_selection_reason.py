from enum import Enum

class OutgoingNumberSelectionResponse_selectionReason(str, Enum):
    StickyConversation = "StickyConversation",
    LeadAssigned = "LeadAssigned",
    CampaignOrSource = "CampaignOrSource",
    Preferred = "Preferred",
    LocalArea = "LocalArea",
    HealthyPool = "HealthyPool",
    FallbackDefault = "FallbackDefault",
    ManualOverride = "ManualOverride",

