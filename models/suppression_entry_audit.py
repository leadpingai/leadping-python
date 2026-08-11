from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .suppression_entry_audit_safe_metadata import SuppressionEntryAudit_safeMetadata

@dataclass
class SuppressionEntryAudit(AdditionalDataHolder, Parsable):
    """
    Records one auditable change to a recipient suppression entry.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the user or system actor responsible for the change.
    actor_id: Optional[str] = None
    # Unique identifier for this suppression audit record.
    id: Optional[str] = None
    # Human-readable reason recorded for the suppression change.
    reason: Optional[str] = None
    # Non-sensitive metadata that provides additional audit context.
    safe_metadata: Optional[SuppressionEntryAudit_safeMetadata] = None
    # System or workflow that initiated the change.
    source: Optional[str] = None
    # Suppression status established by this change, such as active or released.
    status: Optional[str] = None
    # UTC timestamp when the suppression change occurred.
    timestamp: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SuppressionEntryAudit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SuppressionEntryAudit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SuppressionEntryAudit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .suppression_entry_audit_safe_metadata import SuppressionEntryAudit_safeMetadata

        from .suppression_entry_audit_safe_metadata import SuppressionEntryAudit_safeMetadata

        fields: dict[str, Callable[[Any], None]] = {
            "actorId": lambda n : setattr(self, 'actor_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "safeMetadata": lambda n : setattr(self, 'safe_metadata', n.get_object_value(SuppressionEntryAudit_safeMetadata)),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("reason", self.reason)
        writer.write_object_value("safeMetadata", self.safe_metadata)
        writer.write_str_value("source", self.source)
        writer.write_str_value("status", self.status)
        writer.write_datetime_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

