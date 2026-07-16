from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerLeadSourceBreakdown(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Number of leads represented by this Leadping customer lead source breakdown.
    leads: Optional[int] = None
    # Percent expressed as a percentage.
    percent: Optional[float] = None
    # Source classification for this Leadping customer lead source breakdown.
    source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerLeadSourceBreakdown:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerLeadSourceBreakdown
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerLeadSourceBreakdown()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "leads": lambda n : setattr(self, 'leads', n.get_int_value()),
            "percent": lambda n : setattr(self, 'percent', n.get_float_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_int_value("leads", self.leads)
        writer.write_float_value("percent", self.percent)
        writer.write_str_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

