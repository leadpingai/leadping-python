from enum import Enum

class BusinessTableRow_setupStep(str, Enum):
    DomainFinding = "DomainFinding",
    DomainOptionsFound = "DomainOptionsFound",
    SiteGenerating = "SiteGenerating",
    SiteGenerated = "SiteGenerated",
    BrandSubmitted = "BrandSubmitted",
    BrandApproved = "BrandApproved",
    CampaignSubmitted = "CampaignSubmitted",
    CampaignApproved = "CampaignApproved",
    CarrierReviewing = "CarrierReviewing",
    TenDlcComplete = "TenDlcComplete",
    Complete = "Complete",

