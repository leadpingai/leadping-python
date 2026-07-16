from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SuppressionEntryRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for suppression entry.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The business ID associated with this ion entry.
    business_id: Optional[str] = None
    # The channel value for this ion entry.
    channel: Optional[str] = None
    # The email address associated with this ion entry.
    email: Optional[str] = None
    # The phone number associated with this ion entry.
    phone_number: Optional[str] = None
    # The human-readable reason explaining this ion entry.
    reason: Optional[str] = None
    # The recipient identifier value for this ion entry.
    recipient_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SuppressionEntryRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SuppressionEntryRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SuppressionEntryRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "channel": lambda n : setattr(self, 'channel', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recipientIdentifier": lambda n : setattr(self, 'recipient_identifier', n.get_str_value()),
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
        writer.write_str_value("channel", self.channel)
        writer.write_str_value("email", self.email)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recipientIdentifier", self.recipient_identifier)
        writer.write_additional_data_value(self.additional_data)
    

