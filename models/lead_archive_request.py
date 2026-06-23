from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LeadArchiveRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for archiving a lead without deleting its history.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional internal note explaining the archive decision.
    note: Optional[str] = None
    # Reason the lead should leave the active working pipeline.
    reason: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadArchiveRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadArchiveRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadArchiveRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_int_value()),
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
        writer.write_str_value("note", self.note)
        writer.write_int_value("reason", self.reason)
        writer.write_additional_data_value(self.additional_data)
    

