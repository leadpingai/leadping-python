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
    Describes a recipient suppression that prevents outreach through one or more communication channels.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Chronological audit history of suppression and release changes.
    audit: Optional[list[SuppressionEntryAudit]] = None
    # Communication channel affected by the suppression, such as SMS, voice, email, or all channels.
    channel: Optional[str] = None
    # Unique Leadping identifier for the suppression entry.
    id: Optional[str] = None
    # Suppressed email address normalized for matching.
    normalized_email: Optional[str] = None
    # Suppressed phone number normalized to a consistent format.
    normalized_phone_number: Optional[str] = None
    # Identifier of the organization that owns the suppression entry.
    organization_id: Optional[str] = None
    # Human-readable reason the recipient was suppressed or subsequently released.
    reason: Optional[str] = None
    # Provider or customer identifier used to recognize the suppressed recipient.
    recipient_identifier: Optional[str] = None
    # UTC timestamp when the suppression was released, or null while it remains active.
    released_at: Optional[datetime.datetime] = None
    # System or workflow that created the suppression.
    source: Optional[str] = None
    # Current lifecycle state, such as active or released.
    status: Optional[str] = None
    # UTC timestamp when the suppression became active.
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
            "channel": lambda n : setattr(self, 'channel', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "normalizedEmail": lambda n : setattr(self, 'normalized_email', n.get_str_value()),
            "normalizedPhoneNumber": lambda n : setattr(self, 'normalized_phone_number', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "recipientIdentifier": lambda n : setattr(self, 'recipient_identifier', n.get_str_value()),
            "releasedAt": lambda n : setattr(self, 'released_at', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_str_value("channel", self.channel)
        writer.write_str_value("id", self.id)
        writer.write_str_value("normalizedEmail", self.normalized_email)
        writer.write_str_value("normalizedPhoneNumber", self.normalized_phone_number)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("recipientIdentifier", self.recipient_identifier)
        writer.write_datetime_value("releasedAt", self.released_at)
        writer.write_str_value("source", self.source)
        writer.write_str_value("status", self.status)
        writer.write_datetime_value("suppressedAt", self.suppressed_at)
        writer.write_additional_data_value(self.additional_data)
    

