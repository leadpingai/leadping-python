from enum import Enum

class BusinessTableRow_websiteStatus(str, Enum):
    NotStarted = "NotStarted",
    DomainSuggestionsPending = "DomainSuggestionsPending",
    DomainSelectionPending = "DomainSelectionPending",
    DomainPurchasePending = "DomainPurchasePending",
    DomainPurchased = "DomainPurchased",
    WebsiteGenerationQueued = "WebsiteGenerationQueued",
    WebsiteGenerating = "WebsiteGenerating",
    WebsiteDeploymentQueued = "WebsiteDeploymentQueued",
    WebsiteDeploying = "WebsiteDeploying",
    WebsiteLive = "WebsiteLive",
    WebsiteFailed = "WebsiteFailed",
    ManuallyBypassed = "ManuallyBypassed",

