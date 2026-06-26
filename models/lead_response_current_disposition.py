from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .current_disposition_summary import CurrentDispositionSummary

from .current_disposition_summary import CurrentDispositionSummary

@dataclass
class LeadResponse_currentDisposition(CurrentDispositionSummary, Parsable):
    """
    Current disposition summary that describes the lead outcome.
    """
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadResponse_currentDisposition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadResponse_currentDisposition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadResponse_currentDisposition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .current_disposition_summary import CurrentDispositionSummary

        from .current_disposition_summary import CurrentDispositionSummary

        fields: dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

