from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_billing_state_dunning import BusinessBillingState_dunning

@dataclass
class BusinessBillingState(AdditionalDataHolder, Parsable):
    """
    Customer-safe billing state for a Leadping business.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Gets or sets when the active subscription is scheduled to cancel.
    cancel_at: Optional[datetime.datetime] = None
    # Gets or sets the customer-safe payment recovery state for the business.
    dunning: Optional[BusinessBillingState_dunning] = None
    # Indicates whether the business has a saved default payment method.
    has_payment_method: Optional[bool] = None
    # Indicates whether the business has a Stripe customer account.
    has_stripe_customer: Optional[bool] = None
    # Gets or sets when Leadping last processed a payment-method event for the business.
    last_payment_method_event_at: Optional[datetime.datetime] = None
    # Gets or sets when Leadping last processed a subscription event for the business.
    last_subscription_event_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessBillingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessBillingState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessBillingState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_billing_state_dunning import BusinessBillingState_dunning

        from .business_billing_state_dunning import BusinessBillingState_dunning

        fields: dict[str, Callable[[Any], None]] = {
            "cancelAt": lambda n : setattr(self, 'cancel_at', n.get_datetime_value()),
            "dunning": lambda n : setattr(self, 'dunning', n.get_object_value(BusinessBillingState_dunning)),
            "hasPaymentMethod": lambda n : setattr(self, 'has_payment_method', n.get_bool_value()),
            "hasStripeCustomer": lambda n : setattr(self, 'has_stripe_customer', n.get_bool_value()),
            "lastPaymentMethodEventAt": lambda n : setattr(self, 'last_payment_method_event_at', n.get_datetime_value()),
            "lastSubscriptionEventAt": lambda n : setattr(self, 'last_subscription_event_at', n.get_datetime_value()),
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
        writer.write_datetime_value("cancelAt", self.cancel_at)
        writer.write_object_value("dunning", self.dunning)
        writer.write_bool_value("hasPaymentMethod", self.has_payment_method)
        writer.write_bool_value("hasStripeCustomer", self.has_stripe_customer)
        writer.write_datetime_value("lastPaymentMethodEventAt", self.last_payment_method_event_at)
        writer.write_datetime_value("lastSubscriptionEventAt", self.last_subscription_event_at)
        writer.write_additional_data_value(self.additional_data)
    

