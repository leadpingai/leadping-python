from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_stripe_info_cancellation import BusinessStripeInfo_cancellation
    from .business_stripe_info_dunning import BusinessStripeInfo_dunning

@dataclass
class BusinessStripeInfo(AdditionalDataHolder, Parsable):
    """
    Stripe billing state owned by a business account.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The businessUserSubscriptionItemId property
    business_user_subscription_item_id: Optional[str] = None
    # The cancelAt property
    cancel_at: Optional[datetime.datetime] = None
    # Captured subscription cancellation feedback for retention and churn analysis.
    cancellation: Optional[BusinessStripeInfo_cancellation] = None
    # The customerId property
    customer_id: Optional[str] = None
    # The defaultPaymentMethodId property
    default_payment_method_id: Optional[str] = None
    # Dunning state recorded after a failed recurring payment.
    dunning: Optional[BusinessStripeInfo_dunning] = None
    # The lastPaymentMethodEventAt property
    last_payment_method_event_at: Optional[datetime.datetime] = None
    # The lastSubscriptionEventAt property
    last_subscription_event_at: Optional[datetime.datetime] = None
    # The phoneSubscriptionId property
    phone_subscription_id: Optional[str] = None
    # The phoneSubscriptionItemId property
    phone_subscription_item_id: Optional[str] = None
    # The planSubscriptionId property
    plan_subscription_id: Optional[str] = None
    # The planSubscriptionItemId property
    plan_subscription_item_id: Optional[str] = None
    # The subscriptionIds property
    subscription_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessStripeInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessStripeInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BusinessStripeInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .business_stripe_info_cancellation import BusinessStripeInfo_cancellation
        from .business_stripe_info_dunning import BusinessStripeInfo_dunning

        from .business_stripe_info_cancellation import BusinessStripeInfo_cancellation
        from .business_stripe_info_dunning import BusinessStripeInfo_dunning

        fields: dict[str, Callable[[Any], None]] = {
            "businessUserSubscriptionItemId": lambda n : setattr(self, 'business_user_subscription_item_id', n.get_str_value()),
            "cancelAt": lambda n : setattr(self, 'cancel_at', n.get_datetime_value()),
            "cancellation": lambda n : setattr(self, 'cancellation', n.get_object_value(BusinessStripeInfo_cancellation)),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_str_value()),
            "defaultPaymentMethodId": lambda n : setattr(self, 'default_payment_method_id', n.get_str_value()),
            "dunning": lambda n : setattr(self, 'dunning', n.get_object_value(BusinessStripeInfo_dunning)),
            "lastPaymentMethodEventAt": lambda n : setattr(self, 'last_payment_method_event_at', n.get_datetime_value()),
            "lastSubscriptionEventAt": lambda n : setattr(self, 'last_subscription_event_at', n.get_datetime_value()),
            "phoneSubscriptionId": lambda n : setattr(self, 'phone_subscription_id', n.get_str_value()),
            "phoneSubscriptionItemId": lambda n : setattr(self, 'phone_subscription_item_id', n.get_str_value()),
            "planSubscriptionId": lambda n : setattr(self, 'plan_subscription_id', n.get_str_value()),
            "planSubscriptionItemId": lambda n : setattr(self, 'plan_subscription_item_id', n.get_str_value()),
            "subscriptionIds": lambda n : setattr(self, 'subscription_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("businessUserSubscriptionItemId", self.business_user_subscription_item_id)
        writer.write_datetime_value("cancelAt", self.cancel_at)
        writer.write_object_value("cancellation", self.cancellation)
        writer.write_str_value("customerId", self.customer_id)
        writer.write_str_value("defaultPaymentMethodId", self.default_payment_method_id)
        writer.write_object_value("dunning", self.dunning)
        writer.write_datetime_value("lastPaymentMethodEventAt", self.last_payment_method_event_at)
        writer.write_datetime_value("lastSubscriptionEventAt", self.last_subscription_event_at)
        writer.write_str_value("phoneSubscriptionId", self.phone_subscription_id)
        writer.write_str_value("phoneSubscriptionItemId", self.phone_subscription_item_id)
        writer.write_str_value("planSubscriptionId", self.plan_subscription_id)
        writer.write_str_value("planSubscriptionItemId", self.plan_subscription_item_id)
        writer.write_collection_of_primitive_values("subscriptionIds", self.subscription_ids)
        writer.write_additional_data_value(self.additional_data)
    

