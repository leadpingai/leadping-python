from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .suppression_entry_request_safe_metadata import SuppressionEntryRequest_safeMetadata

@dataclass
class SuppressionEntryRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for suppression entry.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actor ID associated with this ion entry.
    actor_id: Optional[str] = None
    # The business ID associated with this ion entry.
    business_id: Optional[str] = None
    # The channel value for this ion entry.
    channel: Optional[str] = None
    # The email address associated with this ion entry.
    email: Optional[str] = None
    # The phone number associated with this ion entry.
    phone_number: Optional[str] = None
    # The provider event ID associated with this ion entry.
    provider_event_id: Optional[str] = None
    # The human-readable reason explaining this ion entry.
    reason: Optional[str] = None
    # The recipient identifier value for this ion entry.
    recipient_identifier: Optional[str] = None
    # The safe metadata key-value data carried with this ion entry; values must be safe to expose in API responses.
    safe_metadata: Optional[SuppressionEntryRequest_safeMetadata] = None
    # The source value for this ion entry.
    source: Optional[str] = None
    # The source event ID associated with this ion entry.
    source_event_id: Optional[str] = None
    # The date and time for the timestamp value on this ion entry.
    timestamp: Optional[datetime.datetime] = None
    
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
        from .suppression_entry_request_safe_metadata import SuppressionEntryRequest_safeMetadata

        from .suppression_entry_request_safe_metadata import SuppressionEntryRequest_safeMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "actorId": lambda n : setattr(self, 'actor_id', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "channel": lambda n : setattr(self, 'channel', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "providerEventId": lambda n : setattr(self, 'provider_event_id', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recipientIdentifier": lambda n : setattr(self, 'recipient_identifier', n.get_str_value()),
            "safeMetadata": lambda n : setattr(self, 'safe_metadata', n.get_object_value(SuppressionEntryRequest_safeMetadata)),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "sourceEventId": lambda n : setattr(self, 'source_event_id', n.get_str_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
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
        writer.write_str_value("actorId", self.actor_id)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("channel", self.channel)
        writer.write_str_value("email", self.email)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("providerEventId", self.provider_event_id)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recipientIdentifier", self.recipient_identifier)
        writer.write_object_value("safeMetadata", self.safe_metadata)
        writer.write_str_value("source", self.source)
        writer.write_str_value("sourceEventId", self.source_event_id)
        writer.write_datetime_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

