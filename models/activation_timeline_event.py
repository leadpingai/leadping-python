from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ActivationTimelineEvent(AdditionalDataHolder, Parsable):
    """
    API DTO containing activation timeline event data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actor name value for this activation timeline event.
    actor_name: Optional[str] = None
    # The date and time for the created at value on this activation timeline event.
    created_at: Optional[datetime.datetime] = None
    # The details value for this activation timeline event.
    details: Optional[str] = None
    # The human-readable failure reason explaining this activation timeline event.
    failure_reason: Optional[str] = None
    # The unique ID for this activation timeline event.
    id: Optional[str] = None
    # The current status for this activation timeline event.
    status: Optional[str] = None
    # The title value for this activation timeline event.
    title: Optional[str] = None
    # The type classification for this activation timeline event.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivationTimelineEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivationTimelineEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActivationTimelineEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actorName": lambda n : setattr(self, 'actor_name', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "details": lambda n : setattr(self, 'details', n.get_str_value()),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("actorName", self.actor_name)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("details", self.details)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_str_value("id", self.id)
        writer.write_str_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

