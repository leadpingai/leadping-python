from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SuppressionEntryRequest(AdditionalDataHolder, Parsable):
    """
    Defines a recipient and communication channel to suppress, release, or check before Leadping sends outreach.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Communication channel affected by the suppression, such as SMS, voice, email, or all channels.
    channel: Optional[str] = None
    # Recipient email address to suppress or check.
    email: Optional[str] = None
    # Organization whose suppression list should be used.
    organization_id: Optional[str] = None
    # Recipient phone number to suppress or check, preferably in E.164 format.
    phone_number: Optional[str] = None
    # Human-readable reason for creating or releasing the suppression.
    reason: Optional[str] = None
    # Optional provider or customer identifier that uniquely identifies the recipient.
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
            "channel": lambda n : setattr(self, 'channel', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
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
        writer.write_str_value("channel", self.channel)
        writer.write_str_value("email", self.email)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recipientIdentifier", self.recipient_identifier)
        writer.write_additional_data_value(self.additional_data)
    

