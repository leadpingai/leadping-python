from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneNumberBillingAttribution(AdditionalDataHolder, Parsable):
    """
    API DTO containing phone number billing attribution data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The business ID associated with this phone number billing attribution.
    business_id: Optional[str] = None
    # The business name value for this phone number billing attribution.
    business_name: Optional[str] = None
    # The channel value for this phone number billing attribution.
    channel: Optional[str] = None
    # The subscription item ID associated with this phone number billing attribution.
    subscription_item_id: Optional[str] = None
    # The user ID associated with this phone number billing attribution.
    user_id: Optional[str] = None
    # The user name value for this phone number billing attribution.
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberBillingAttribution:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberBillingAttribution
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberBillingAttribution()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "businessName": lambda n : setattr(self, 'business_name', n.get_str_value()),
            "channel": lambda n : setattr(self, 'channel', n.get_str_value()),
            "subscriptionItemId": lambda n : setattr(self, 'subscription_item_id', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("businessName", self.business_name)
        writer.write_str_value("channel", self.channel)
        writer.write_str_value("subscriptionItemId", self.subscription_item_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_additional_data_value(self.additional_data)
    

