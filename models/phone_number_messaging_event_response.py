from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneNumberMessagingEventResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API phone number messaging event returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp when this phone number messaging event was created.
    created_at: Optional[datetime.datetime] = None
    # Communication direction for this phone number messaging event, such as inbound or outbound.
    direction: Optional[str] = None
    # Event type used to classify this timeline, SMS, call, or automation event.
    event_type: Optional[str] = None
    # Sender phone number used for this communication.
    from_phone_number: Optional[str] = None
    # Unique Leadping identifier for this phone number messaging event.
    id: Optional[str] = None
    # Indicates whether the recipient has opted out of further SMS communication.
    is_opt_out: Optional[bool] = None
    # Short display label for this phone number messaging event, formatted for charts, filters, or list views.
    label: Optional[str] = None
    # Provider lifecycle or delivery status for this phone number messaging event.
    provider_status: Optional[str] = None
    # Short preview of the SMS or conversation text for this phone number messaging event.
    text_preview: Optional[str] = None
    # Recipient phone number used for this communication.
    to_phone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberMessagingEventResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberMessagingEventResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberMessagingEventResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "eventType": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isOptOut": lambda n : setattr(self, 'is_opt_out', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "providerStatus": lambda n : setattr(self, 'provider_status', n.get_str_value()),
            "textPreview": lambda n : setattr(self, 'text_preview', n.get_str_value()),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
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
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("direction", self.direction)
        writer.write_str_value("eventType", self.event_type)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isOptOut", self.is_opt_out)
        writer.write_str_value("label", self.label)
        writer.write_str_value("providerStatus", self.provider_status)
        writer.write_str_value("textPreview", self.text_preview)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_additional_data_value(self.additional_data)
    

