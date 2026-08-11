from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization_billing_state_dunning import OrganizationBillingState_dunning
    from .organization_billing_state_pending_billing_plan import OrganizationBillingState_pendingBillingPlan

@dataclass
class OrganizationBillingState(AdditionalDataHolder, Parsable):
    """
    Customer-safe billing state for a Leadping organization.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Date and time when the scheduled billing plan change takes effect.
    billing_plan_change_effective_at: Optional[datetime.datetime] = None
    # UTC timestamp when the active subscription is scheduled to cancel.
    cancel_at: Optional[datetime.datetime] = None
    # Customer-safe payment recovery state for the organization.
    dunning: Optional[OrganizationBillingState_dunning] = None
    # Indicates whether the organization has a saved default payment method.
    has_payment_method: Optional[bool] = None
    # Indicates whether the organization has a Stripe customer account.
    has_stripe_customer: Optional[bool] = None
    # UTC timestamp when Leadping last processed a payment-method event for the organization.
    last_payment_method_event_at: Optional[datetime.datetime] = None
    # UTC timestamp when Leadping last processed a subscription event for the organization.
    last_subscription_event_at: Optional[datetime.datetime] = None
    # Defines the supported Billing Plan values.
    pending_billing_plan: Optional[OrganizationBillingState_pendingBillingPlan] = None
    # Start of the current plan billing period.
    plan_period_start_at: Optional[datetime.datetime] = None
    # Current plan renewal date.
    plan_renewal_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationBillingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationBillingState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationBillingState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organization_billing_state_dunning import OrganizationBillingState_dunning
        from .organization_billing_state_pending_billing_plan import OrganizationBillingState_pendingBillingPlan

        from .organization_billing_state_dunning import OrganizationBillingState_dunning
        from .organization_billing_state_pending_billing_plan import OrganizationBillingState_pendingBillingPlan

        fields: dict[str, Callable[[Any], None]] = {
            "billingPlanChangeEffectiveAt": lambda n : setattr(self, 'billing_plan_change_effective_at', n.get_datetime_value()),
            "cancelAt": lambda n : setattr(self, 'cancel_at', n.get_datetime_value()),
            "dunning": lambda n : setattr(self, 'dunning', n.get_object_value(OrganizationBillingState_dunning)),
            "hasPaymentMethod": lambda n : setattr(self, 'has_payment_method', n.get_bool_value()),
            "hasStripeCustomer": lambda n : setattr(self, 'has_stripe_customer', n.get_bool_value()),
            "lastPaymentMethodEventAt": lambda n : setattr(self, 'last_payment_method_event_at', n.get_datetime_value()),
            "lastSubscriptionEventAt": lambda n : setattr(self, 'last_subscription_event_at', n.get_datetime_value()),
            "pendingBillingPlan": lambda n : setattr(self, 'pending_billing_plan', n.get_enum_value(OrganizationBillingState_pendingBillingPlan)),
            "planPeriodStartAt": lambda n : setattr(self, 'plan_period_start_at', n.get_datetime_value()),
            "planRenewalAt": lambda n : setattr(self, 'plan_renewal_at', n.get_datetime_value()),
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
        writer.write_datetime_value("billingPlanChangeEffectiveAt", self.billing_plan_change_effective_at)
        writer.write_datetime_value("cancelAt", self.cancel_at)
        writer.write_object_value("dunning", self.dunning)
        writer.write_bool_value("hasPaymentMethod", self.has_payment_method)
        writer.write_bool_value("hasStripeCustomer", self.has_stripe_customer)
        writer.write_datetime_value("lastPaymentMethodEventAt", self.last_payment_method_event_at)
        writer.write_datetime_value("lastSubscriptionEventAt", self.last_subscription_event_at)
        writer.write_enum_value("pendingBillingPlan", self.pending_billing_plan)
        writer.write_datetime_value("planPeriodStartAt", self.plan_period_start_at)
        writer.write_datetime_value("planRenewalAt", self.plan_renewal_at)
        writer.write_additional_data_value(self.additional_data)
    

