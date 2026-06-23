from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_subscription_cancellation_info import UserSubscriptionCancellationInfo

from .user_subscription_cancellation_info import UserSubscriptionCancellationInfo

@dataclass
class UserStripeInfo_cancellation(UserSubscriptionCancellationInfo, Parsable):
    """
    The captured subscription cancellation feedback for retention and churn analysis.
    """
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserStripeInfo_cancellation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserStripeInfo_cancellation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserStripeInfo_cancellation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_subscription_cancellation_info import UserSubscriptionCancellationInfo

        from .user_subscription_cancellation_info import UserSubscriptionCancellationInfo

        fields: dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

