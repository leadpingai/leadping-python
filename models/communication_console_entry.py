from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CommunicationConsoleEntry(AdditionalDataHolder, Parsable):
    """
    Describes one durable diagnostic entry from the processing of a communication.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier of this diagnostic console entry.
    id: Optional[str] = None
    # User-safe diagnostic message describing what occurred at this stage.
    message: Optional[str] = None
    # UTC timestamp when this communication-processing event occurred.
    occurred_at: Optional[datetime.datetime] = None
    # Communication-processing stage that produced the entry, such as validation, routing, or provider delivery.
    stage: Optional[str] = None
    # Outcome or state recorded for this processing stage.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CommunicationConsoleEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationConsoleEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CommunicationConsoleEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "occurredAt": lambda n : setattr(self, 'occurred_at', n.get_datetime_value()),
            "stage": lambda n : setattr(self, 'stage', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("message", self.message)
        writer.write_datetime_value("occurredAt", self.occurred_at)
        writer.write_str_value("stage", self.stage)
        writer.write_str_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

