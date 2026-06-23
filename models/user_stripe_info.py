from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_stripe_info_cancellation import UserStripeInfo_cancellation
    from .user_stripe_info_dunning import UserStripeInfo_dunning

@dataclass
class UserStripeInfo(AdditionalDataHolder, Parsable):
    """
    API DTO containing user stripe info data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The business user subscription item ID associated with this user Stripe info.
    business_user_subscription_item_id: Optional[str] = None
    # The date and time for the cancel at value on this user Stripe info.
    cancel_at: Optional[datetime.datetime] = None
    # The captured subscription cancellation feedback for retention and churn analysis.
    cancellation: Optional[UserStripeInfo_cancellation] = None
    # The customer ID associated with this user Stripe info.
    customer_id: Optional[str] = None
    # The default payment method ID associated with this user Stripe info.
    default_payment_method_id: Optional[str] = None
    # The active dunning state after a failed recurring payment.
    dunning: Optional[UserStripeInfo_dunning] = None
    # The date and time for the last payment method event at value on this user Stripe info.
    last_payment_method_event_at: Optional[datetime.datetime] = None
    # The date and time for the last subscription event at value on this user Stripe info.
    last_subscription_event_at: Optional[datetime.datetime] = None
    # The phone subscription ID associated with this user Stripe info.
    phone_subscription_id: Optional[str] = None
    # The phone subscription item ID associated with this user Stripe info.
    phone_subscription_item_id: Optional[str] = None
    # The plan subscription ID associated with this user Stripe info.
    plan_subscription_id: Optional[str] = None
    # The plan subscription item ID associated with this user Stripe info.
    plan_subscription_item_id: Optional[str] = None
    # The subscription ids included with this user Stripe info.
    subscription_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserStripeInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserStripeInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserStripeInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_stripe_info_cancellation import UserStripeInfo_cancellation
        from .user_stripe_info_dunning import UserStripeInfo_dunning

        from .user_stripe_info_cancellation import UserStripeInfo_cancellation
        from .user_stripe_info_dunning import UserStripeInfo_dunning

        fields: dict[str, Callable[[Any], None]] = {
            "businessUserSubscriptionItemId": lambda n : setattr(self, 'business_user_subscription_item_id', n.get_str_value()),
            "cancelAt": lambda n : setattr(self, 'cancel_at', n.get_datetime_value()),
            "cancellation": lambda n : setattr(self, 'cancellation', n.get_object_value(UserStripeInfo_cancellation)),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_str_value()),
            "defaultPaymentMethodId": lambda n : setattr(self, 'default_payment_method_id', n.get_str_value()),
            "dunning": lambda n : setattr(self, 'dunning', n.get_object_value(UserStripeInfo_dunning)),
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
    

