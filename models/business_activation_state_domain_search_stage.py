from enum import Enum

class BusinessActivationState_domainSearchStage(str, Enum):
    Queued = "Queued",
    AskingOpenAi = "AskingOpenAi",
    CheckingCloudflare = "CheckingCloudflare",
    Ranking = "Ranking",
    Complete = "Complete",
    Failed = "Failed",

