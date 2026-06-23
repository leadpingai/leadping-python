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
    from .business_activation_state_ten_dlc_draft import BusinessActivationState_tenDlcDraft
    from .customer_activation_status import CustomerActivationStatus
    from .ten_dlc_application_status import TenDlcApplicationStatus
    from .website_lifecycle_status import WebsiteLifecycleStatus

@dataclass
class BusinessActivationState(AdditionalDataHolder, Parsable):
    """
    API DTO containing business activation state data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time for the activated at value on this business activation state.
    activated_at: Optional[datetime.datetime] = None
    # The current billing subscription status for this business activation state.
    billing_subscription_status: Optional[ActivationSubscriptionStatus] = None
    # The business description value for this business activation state.
    business_description: Optional[str] = None
    # The compliance notes value for this business activation state.
    compliance_notes: Optional[str] = None
    # Whether controlled launch applies to this business activation state.
    controlled_launch: Optional[bool] = None
    # The date and time for the created at value on this business activation state.
    created_at: Optional[datetime.datetime] = None
    # The current customer facing status for this business activation state.
    customer_facing_status: Optional[str] = None
    # The date and time for the domain approved at value on this business activation state.
    domain_approved_at: Optional[datetime.datetime] = None
    # The domain options included with this business activation state.
    domain_options: Optional[list[ActivationDomainOption]] = None
    # The events included with this business activation state.
    events: Optional[list[ActivationTimelineEvent]] = None
    # The date and time for the failed at value on this business activation state.
    failed_at: Optional[datetime.datetime] = None
    # The industry value for this business activation state.
    industry: Optional[str] = None
    # The date and time for the launch approved at value on this business activation state.
    launch_approved_at: Optional[datetime.datetime] = None
    # The date and time for the launch review requested at value on this business activation state.
    launch_review_requested_at: Optional[datetime.datetime] = None
    # The current launch review status for this business activation state.
    launch_review_status: Optional[ActivationLaunchReviewStatus] = None
    # The offer value for this business activation state.
    offer: Optional[str] = None
    # The current onboarding status for this business activation state.
    onboarding_status: Optional[ActivationOnboardingStatus] = None
    # The date and time for the payment method confirmed at value on this business activation state.
    payment_method_confirmed_at: Optional[datetime.datetime] = None
    # The current payment status for this business activation state.
    payment_status: Optional[ActivationPaymentStatus] = None
    # The selected domain value for this business activation state.
    selected_domain: Optional[str] = None
    # The service area value for this business activation state.
    service_area: Optional[str] = None
    # The current status for this business activation state.
    status: Optional[CustomerActivationStatus] = None
    # The date and time for the subscription active at value on this business activation state.
    subscription_active_at: Optional[datetime.datetime] = None
    # The date and time for the subscription pending at value on this business activation state.
    subscription_pending_at: Optional[datetime.datetime] = None
    # The target audience value for this business activation state.
    target_audience: Optional[str] = None
    # The date and time for the telephony partially provisioned at value on this business activation state.
    telephony_partially_provisioned_at: Optional[datetime.datetime] = None
    # The date and time for the telephony provisioning started at value on this business activation state.
    telephony_provisioning_started_at: Optional[datetime.datetime] = None
    # The date and time for the telephony ready at value on this business activation state.
    telephony_ready_at: Optional[datetime.datetime] = None
    # The current telephony status for this business activation state.
    telephony_status: Optional[ActivationTelephonyStatus] = None
    # The 10DLC draft value for this business activation state.
    ten_dlc_draft: Optional[BusinessActivationState_tenDlcDraft] = None
    # The current 10DLC status for this business activation state.
    ten_dlc_status: Optional[TenDlcApplicationStatus] = None
    # The date and time for the updated at value on this business activation state.
    updated_at: Optional[datetime.datetime] = None
    # The website needs value for this business activation state.
    website_needs: Optional[str] = None
    # The current website status for this business activation state.
    website_status: Optional[WebsiteLifecycleStatus] = None
    # The URL associated with this business activation state.
    website_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessActivationState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessActivationState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessActivationState()
    
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
        from .business_activation_state_ten_dlc_draft import BusinessActivationState_tenDlcDraft
        from .customer_activation_status import CustomerActivationStatus
        from .ten_dlc_application_status import TenDlcApplicationStatus
        from .website_lifecycle_status import WebsiteLifecycleStatus

        from .activation_domain_option import ActivationDomainOption
        from .activation_launch_review_status import ActivationLaunchReviewStatus
        from .activation_onboarding_status import ActivationOnboardingStatus
        from .activation_payment_status import ActivationPaymentStatus
        from .activation_subscription_status import ActivationSubscriptionStatus
        from .activation_telephony_status import ActivationTelephonyStatus
        from .activation_timeline_event import ActivationTimelineEvent
        from .business_activation_state_ten_dlc_draft import BusinessActivationState_tenDlcDraft
        from .customer_activation_status import CustomerActivationStatus
        from .ten_dlc_application_status import TenDlcApplicationStatus
        from .website_lifecycle_status import WebsiteLifecycleStatus

        fields: dict[str, Callable[[Any], None]] = {
            "activatedAt": lambda n : setattr(self, 'activated_at', n.get_datetime_value()),
            "billingSubscriptionStatus": lambda n : setattr(self, 'billing_subscription_status', n.get_enum_value(ActivationSubscriptionStatus)),
            "businessDescription": lambda n : setattr(self, 'business_description', n.get_str_value()),
            "complianceNotes": lambda n : setattr(self, 'compliance_notes', n.get_str_value()),
            "controlledLaunch": lambda n : setattr(self, 'controlled_launch', n.get_bool_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "customerFacingStatus": lambda n : setattr(self, 'customer_facing_status', n.get_str_value()),
            "domainApprovedAt": lambda n : setattr(self, 'domain_approved_at', n.get_datetime_value()),
            "domainOptions": lambda n : setattr(self, 'domain_options', n.get_collection_of_object_values(ActivationDomainOption)),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(ActivationTimelineEvent)),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "launchApprovedAt": lambda n : setattr(self, 'launch_approved_at', n.get_datetime_value()),
            "launchReviewRequestedAt": lambda n : setattr(self, 'launch_review_requested_at', n.get_datetime_value()),
            "launchReviewStatus": lambda n : setattr(self, 'launch_review_status', n.get_enum_value(ActivationLaunchReviewStatus)),
            "offer": lambda n : setattr(self, 'offer', n.get_str_value()),
            "onboardingStatus": lambda n : setattr(self, 'onboarding_status', n.get_enum_value(ActivationOnboardingStatus)),
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
            "tenDlcDraft": lambda n : setattr(self, 'ten_dlc_draft', n.get_object_value(BusinessActivationState_tenDlcDraft)),
            "tenDlcStatus": lambda n : setattr(self, 'ten_dlc_status', n.get_enum_value(TenDlcApplicationStatus)),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
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
        writer.write_str_value("businessDescription", self.business_description)
        writer.write_str_value("complianceNotes", self.compliance_notes)
        writer.write_bool_value("controlledLaunch", self.controlled_launch)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("customerFacingStatus", self.customer_facing_status)
        writer.write_datetime_value("domainApprovedAt", self.domain_approved_at)
        writer.write_collection_of_object_values("domainOptions", self.domain_options)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("industry", self.industry)
        writer.write_datetime_value("launchApprovedAt", self.launch_approved_at)
        writer.write_datetime_value("launchReviewRequestedAt", self.launch_review_requested_at)
        writer.write_enum_value("launchReviewStatus", self.launch_review_status)
        writer.write_str_value("offer", self.offer)
        writer.write_enum_value("onboardingStatus", self.onboarding_status)
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
        writer.write_object_value("tenDlcDraft", self.ten_dlc_draft)
        writer.write_enum_value("tenDlcStatus", self.ten_dlc_status)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_str_value("websiteNeeds", self.website_needs)
        writer.write_enum_value("websiteStatus", self.website_status)
        writer.write_str_value("websiteUrl", self.website_url)
        writer.write_additional_data_value(self.additional_data)
    

