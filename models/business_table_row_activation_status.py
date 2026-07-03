from enum import Enum

class BusinessTableRow_activationStatus(str, Enum):
    DraftOnboarding = "DraftOnboarding",
    PaymentMethodPending = "PaymentMethodPending",
    PaymentMethodConfirmed = "PaymentMethodConfirmed",
    SubscriptionPending = "SubscriptionPending",
    SubscriptionReceived = "SubscriptionReceived",
    SubscriptionActive = "SubscriptionActive",
    LaunchReviewPending = "LaunchReviewPending",
    TelephonyProvisioningPending = "TelephonyProvisioningPending",
    TelephonyPartiallyProvisioned = "TelephonyPartiallyProvisioned",
    TelephonyReady = "TelephonyReady",
    AwaitingReview = "AwaitingReview",
    DomainSelection = "DomainSelection",
    WebsiteSetup = "WebsiteSetup",
    ComplianceRegistration = "ComplianceRegistration",
    ReadyForApproval = "ReadyForApproval",
    Active = "Active",
    Failed = "Failed",
    Blocked = "Blocked",
    BlockedRequiresOperatorAction = "BlockedRequiresOperatorAction",
    ManuallyBypassed = "ManuallyBypassed",

