from enum import Enum

class OrganizationActivationState_domainSearchStage(str, Enum):
    Queued = "Queued",
    AskingOpenAi = "AskingOpenAi",
    CheckingCloudflare = "CheckingCloudflare",
    Ranking = "Ranking",
    Complete = "Complete",
    Failed = "Failed",

