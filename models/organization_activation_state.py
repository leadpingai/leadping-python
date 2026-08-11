from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activation_domain_option import ActivationDomainOption
    from .activation_launch_review_status import ActivationLaunchReviewStatus
    from .activation_onboarding_status import ActivationOnboardingStatus
    from .activation_payment_status import ActivationPaymentStatus
    from .activation_subscription_status import ActivationSubscriptionStatus
    from .activation_telephony_status import ActivationTelephonyStatus
    from .activation_timeline_event import ActivationTimelineEvent
    from .customer_activation_status import CustomerActivationStatus
    from .organization_activation_state_domain_search_stage import OrganizationActivationState_domainSearchStage
    from .organization_activation_state_ten_dlc_draft import OrganizationActivationState_tenDlcDraft
    from .ten_dlc_application_status import TenDlcApplicationStatus
    from .website_lifecycle_status import WebsiteLifecycleStatus

@dataclass
class OrganizationActivationState(AdditionalDataHolder, Parsable):
    """
    Describes organization activation state data used in Leadping API requests and responses.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp for activated at on this organization activation state.
    activated_at: Optional[datetime.datetime] = None
    # The current billing subscription status for this organization activation state.
    billing_subscription_status: Optional[ActivationSubscriptionStatus] = None
    # Compliance notes for this organization activation state.
    compliance_notes: Optional[str] = None
    # Whether controlled launch applies to this organization activation state.
    controlled_launch: Optional[bool] = None
    # UTC timestamp for created at on this organization activation state.
    created_at: Optional[datetime.datetime] = None
    # The current customer facing status for this organization activation state.
    customer_facing_status: Optional[str] = None
    # UTC timestamp for domain approved at on this organization activation state.
    domain_approved_at: Optional[datetime.datetime] = None
    # The domain options included with this organization activation state.
    domain_options: Optional[list[ActivationDomainOption]] = None
    # The date and time the selected domain was purchased.
    domain_purchased_at: Optional[datetime.datetime] = None
    # Identifies the active domain search run.
    domain_search_id: Optional[str] = None
    # Defines the stages of a domain search.
    domain_search_stage: Optional[OrganizationActivationState_domainSearchStage] = None
    # The last time domain search progress changed.
    domain_search_updated_at: Optional[datetime.datetime] = None
    # The events included with this organization activation state.
    events: Optional[list[ActivationTimelineEvent]] = None
    # UTC timestamp for failed at on this organization activation state.
    failed_at: Optional[datetime.datetime] = None
    # Industry for this organization activation state.
    industry: Optional[str] = None
    # UTC timestamp for launch approved at on this organization activation state.
    launch_approved_at: Optional[datetime.datetime] = None
    # UTC timestamp for launch review requested at on this organization activation state.
    launch_review_requested_at: Optional[datetime.datetime] = None
    # The current launch review status for this organization activation state.
    launch_review_status: Optional[ActivationLaunchReviewStatus] = None
    # Offer for this organization activation state.
    offer: Optional[str] = None
    # The current onboarding status for this organization activation state.
    onboarding_status: Optional[ActivationOnboardingStatus] = None
    # Organization description for this organization activation state.
    organization_description: Optional[str] = None
    # UTC timestamp for payment method confirmed at on this organization activation state.
    payment_method_confirmed_at: Optional[datetime.datetime] = None
    # The current payment status for this organization activation state.
    payment_status: Optional[ActivationPaymentStatus] = None
    # Selected domain for this organization activation state.
    selected_domain: Optional[str] = None
    # Service area for this organization activation state.
    service_area: Optional[str] = None
    # The current status for this organization activation state.
    status: Optional[CustomerActivationStatus] = None
    # UTC timestamp for subscription active at on this organization activation state.
    subscription_active_at: Optional[datetime.datetime] = None
    # UTC timestamp for subscription pending at on this organization activation state.
    subscription_pending_at: Optional[datetime.datetime] = None
    # Target audience for this organization activation state.
    target_audience: Optional[str] = None
    # UTC timestamp for telephony partially provisioned at on this organization activation state.
    telephony_partially_provisioned_at: Optional[datetime.datetime] = None
    # UTC timestamp for telephony provisioning started at on this organization activation state.
    telephony_provisioning_started_at: Optional[datetime.datetime] = None
    # UTC timestamp for telephony ready at on this organization activation state.
    telephony_ready_at: Optional[datetime.datetime] = None
    # The current telephony status for this organization activation state.
    telephony_status: Optional[ActivationTelephonyStatus] = None
    # Identifier of the first-class 10DLC application entity for this organization.
    ten_dlc_application_id: Optional[str] = None
    # 10DLC draft for this organization activation state.
    ten_dlc_draft: Optional[OrganizationActivationState_tenDlcDraft] = None
    # The current 10DLC status for this organization activation state.
    ten_dlc_status: Optional[TenDlcApplicationStatus] = None
    # UTC timestamp for updated at on this organization activation state.
    updated_at: Optional[datetime.datetime] = None
    # The latest persisted website generation progress message.
    website_generation_result: Optional[str] = None
    # Website needs for this organization activation state.
    website_needs: Optional[str] = None
    # The current website status for this organization activation state.
    website_status: Optional[WebsiteLifecycleStatus] = None
    # The URL associated with this organization activation state.
    website_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationActivationState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationActivationState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationActivationState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activation_domain_option import ActivationDomainOption
        from .activation_launch_review_status import ActivationLaunchReviewStatus
        from .activation_onboarding_status import ActivationOnboardingStatus
        from .activation_payment_status import ActivationPaymentStatus
        from .activation_subscription_status import ActivationSubscriptionStatus
        from .activation_telephony_status import ActivationTelephonyStatus
        from .activation_timeline_event import ActivationTimelineEvent
        from .customer_activation_status import CustomerActivationStatus
        from .organization_activation_state_domain_search_stage import OrganizationActivationState_domainSearchStage
        from .organization_activation_state_ten_dlc_draft import OrganizationActivationState_tenDlcDraft
        from .ten_dlc_application_status import TenDlcApplicationStatus
        from .website_lifecycle_status import WebsiteLifecycleStatus

        from .activation_domain_option import ActivationDomainOption
        from .activation_launch_review_status import ActivationLaunchReviewStatus
        from .activation_onboarding_status import ActivationOnboardingStatus
        from .activation_payment_status import ActivationPaymentStatus
        from .activation_subscription_status import ActivationSubscriptionStatus
        from .activation_telephony_status import ActivationTelephonyStatus
        from .activation_timeline_event import ActivationTimelineEvent
        from .customer_activation_status import CustomerActivationStatus
        from .organization_activation_state_domain_search_stage import OrganizationActivationState_domainSearchStage
        from .organization_activation_state_ten_dlc_draft import OrganizationActivationState_tenDlcDraft
        from .ten_dlc_application_status import TenDlcApplicationStatus
        from .website_lifecycle_status import WebsiteLifecycleStatus

        fields: dict[str, Callable[[Any], None]] = {
            "activatedAt": lambda n : setattr(self, 'activated_at', n.get_datetime_value()),
            "billingSubscriptionStatus": lambda n : setattr(self, 'billing_subscription_status', n.get_enum_value(ActivationSubscriptionStatus)),
            "complianceNotes": lambda n : setattr(self, 'compliance_notes', n.get_str_value()),
            "controlledLaunch": lambda n : setattr(self, 'controlled_launch', n.get_bool_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "customerFacingStatus": lambda n : setattr(self, 'customer_facing_status', n.get_str_value()),
            "domainApprovedAt": lambda n : setattr(self, 'domain_approved_at', n.get_datetime_value()),
            "domainOptions": lambda n : setattr(self, 'domain_options', n.get_collection_of_object_values(ActivationDomainOption)),
            "domainPurchasedAt": lambda n : setattr(self, 'domain_purchased_at', n.get_datetime_value()),
            "domainSearchId": lambda n : setattr(self, 'domain_search_id', n.get_str_value()),
            "domainSearchStage": lambda n : setattr(self, 'domain_search_stage', n.get_enum_value(OrganizationActivationState_domainSearchStage)),
            "domainSearchUpdatedAt": lambda n : setattr(self, 'domain_search_updated_at', n.get_datetime_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(ActivationTimelineEvent)),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "launchApprovedAt": lambda n : setattr(self, 'launch_approved_at', n.get_datetime_value()),
            "launchReviewRequestedAt": lambda n : setattr(self, 'launch_review_requested_at', n.get_datetime_value()),
            "launchReviewStatus": lambda n : setattr(self, 'launch_review_status', n.get_enum_value(ActivationLaunchReviewStatus)),
            "offer": lambda n : setattr(self, 'offer', n.get_str_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(ActivationOnboardingStatus)),
            "organizationDescription": lambda n : setattr(self, 'organization_description', n.get_str_value()),
            "paymentMethodConfirmedAt": lambda n : setattr(self, 'payment_method_confirmed_at', n.get_datetime_value()),
            "paymentStatus": lambda n : setattr(self, 'payment_status', n.get_enum_value(ActivationPaymentStatus)),
            "selectedDomain": lambda n : setattr(self, 'selected_domain', n.get_str_value()),
            "serviceArea": lambda n : setattr(self, 'service_area', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CustomerActivationStatus)),
            "subscriptionActiveAt": lambda n : setattr(self, 'subscription_active_at', n.get_datetime_value()),
            "subscriptionPendingAt": lambda n : setattr(self, 'subscription_pending_at', n.get_datetime_value()),
            "targetAudience": lambda n : setattr(self, 'target_audience', n.get_str_value()),
            "telephonyPartiallyProvisionedAt": lambda n : setattr(self, 'telephony_partially_provisioned_at', n.get_datetime_value()),
            "telephonyProvisioningStartedAt": lambda n : setattr(self, 'telephony_provisioning_started_at', n.get_datetime_value()),
            "telephonyReadyAt": lambda n : setattr(self, 'telephony_ready_at', n.get_datetime_value()),
            "telephonyStatus": lambda n : setattr(self, 'telephony_status', n.get_enum_value(ActivationTelephonyStatus)),
            "tenDlcApplicationId": lambda n : setattr(self, 'ten_dlc_application_id', n.get_str_value()),
            "tenDlcDraft": lambda n : setattr(self, 'ten_dlc_draft', n.get_object_value(OrganizationActivationState_tenDlcDraft)),
            "tenDlcStatus": lambda n : setattr(self, 'ten_dlc_status', n.get_enum_value(TenDlcApplicationStatus)),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "websiteGenerationResult": lambda n : setattr(self, 'website_generation_result', n.get_str_value()),
            "websiteNeeds": lambda n : setattr(self, 'website_needs', n.get_str_value()),
            "websiteStatus": lambda n : setattr(self, 'website_status', n.get_enum_value(WebsiteLifecycleStatus)),
            "websiteUrl": lambda n : setattr(self, 'website_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("activatedAt", self.activated_at)
        writer.write_enum_value("billingSubscriptionStatus", self.billing_subscription_status)
        writer.write_str_value("complianceNotes", self.compliance_notes)
        writer.write_bool_value("controlledLaunch", self.controlled_launch)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("customerFacingStatus", self.customer_facing_status)
        writer.write_datetime_value("domainApprovedAt", self.domain_approved_at)
        writer.write_collection_of_object_values("domainOptions", self.domain_options)
        writer.write_datetime_value("domainPurchasedAt", self.domain_purchased_at)
        writer.write_str_value("domainSearchId", self.domain_search_id)
        writer.write_enum_value("domainSearchStage", self.domain_search_stage)
        writer.write_datetime_value("domainSearchUpdatedAt", self.domain_search_updated_at)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("industry", self.industry)
        writer.write_datetime_value("launchApprovedAt", self.launch_approved_at)
        writer.write_datetime_value("launchReviewRequestedAt", self.launch_review_requested_at)
        writer.write_enum_value("launchReviewStatus", self.launch_review_status)
        writer.write_str_value("offer", self.offer)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
        writer.write_str_value("organizationDescription", self.organization_description)
        writer.write_datetime_value("paymentMethodConfirmedAt", self.payment_method_confirmed_at)
        writer.write_enum_value("paymentStatus", self.payment_status)
        writer.write_str_value("selectedDomain", self.selected_domain)
        writer.write_str_value("serviceArea", self.service_area)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("subscriptionActiveAt", self.subscription_active_at)
        writer.write_datetime_value("subscriptionPendingAt", self.subscription_pending_at)
        writer.write_str_value("targetAudience", self.target_audience)
        writer.write_datetime_value("telephonyPartiallyProvisionedAt", self.telephony_partially_provisioned_at)
        writer.write_datetime_value("telephonyProvisioningStartedAt", self.telephony_provisioning_started_at)
        writer.write_datetime_value("telephonyReadyAt", self.telephony_ready_at)
        writer.write_enum_value("telephonyStatus", self.telephony_status)
        writer.write_str_value("tenDlcApplicationId", self.ten_dlc_application_id)
        writer.write_object_value("tenDlcDraft", self.ten_dlc_draft)
        writer.write_enum_value("tenDlcStatus", self.ten_dlc_status)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_str_value("websiteGenerationResult", self.website_generation_result)
        writer.write_str_value("websiteNeeds", self.website_needs)
        writer.write_enum_value("websiteStatus", self.website_status)
        writer.write_str_value("websiteUrl", self.website_url)
        writer.write_additional_data_value(self.additional_data)
    

