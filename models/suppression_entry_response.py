from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .suppression_entry_audit import SuppressionEntryAudit

@dataclass
class SuppressionEntryResponse(AdditionalDataHolder, Parsable):
    """
    API response containing suppression entry data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The audit included with this ion entry.
    audit: Optional[list[SuppressionEntryAudit]] = None
    # The business ID associated with this ion entry.
    business_id: Optional[str] = None
    # The channel value for this ion entry.
    channel: Optional[str] = None
    # The unique ID for this ion entry.
    id: Optional[str] = None
    # The normalized email value for this ion entry.
    normalized_email: Optional[str] = None
    # The phone number associated with this ion entry.
    normalized_phone_number: Optional[str] = None
    # The provider event ID associated with this ion entry.
    provider_event_id: Optional[str] = None
    # The human-readable reason explaining this ion entry.
    reason: Optional[str] = None
    # The recipient identifier value for this ion entry.
    recipient_identifier: Optional[str] = None
    # The date and time for the released at value on this ion entry.
    released_at: Optional[datetime.datetime] = None
    # The source value for this ion entry.
    source: Optional[str] = None
    # The source event ID associated with this ion entry.
    source_event_id: Optional[str] = None
    # The current status for this ion entry.
    status: Optional[str] = None
    # The date and time for the suppressed at value on this ion entry.
    suppressed_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SuppressionEntryResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SuppressionEntryResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SuppressionEntryResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .suppression_entry_audit import SuppressionEntryAudit

        from .suppression_entry_audit import SuppressionEntryAudit

        fields: dict[str, Callable[[Any], None]] = {
            "audit": lambda n : setattr(self, 'audit', n.get_collection_of_object_values(SuppressionEntryAudit)),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "channel": lambda n : setattr(self, 'channel', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "normalizedEmail": lambda n : setattr(self, 'normalized_email', n.get_str_value()),
            "normalizedPhoneNumber": lambda n : setattr(self, 'normalized_phone_number', n.get_str_value()),
            "providerEventId": lambda n : setattr(self, 'provider_event_id', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recipientIdentifier": lambda n : setattr(self, 'recipient_identifier', n.get_str_value()),
            "releasedAt": lambda n : setattr(self, 'released_at', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "sourceEventId": lambda n : setattr(self, 'source_event_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "suppressedAt": lambda n : setattr(self, 'suppressed_at', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("audit", self.audit)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("channel", self.channel)
        writer.write_str_value("id", self.id)
        writer.write_str_value("normalizedEmail", self.normalized_email)
        writer.write_str_value("normalizedPhoneNumber", self.normalized_phone_number)
        writer.write_str_value("providerEventId", self.provider_event_id)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recipientIdentifier", self.recipient_identifier)
        writer.write_datetime_value("releasedAt", self.released_at)
        writer.write_str_value("source", self.source)
        writer.write_str_value("sourceEventId", self.source_event_id)
        writer.write_str_value("status", self.status)
        writer.write_datetime_value("suppressedAt", self.suppressed_at)
        writer.write_additional_data_value(self.additional_data)
    

