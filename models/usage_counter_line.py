from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UsageCounterLine(AdditionalDataHolder, Parsable):
    """
    Describes one named usage total displayed in organization billing and activity summaries.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The stable key for this usage counter.
    key: Optional[str] = None
    # The human-readable label for this usage counter.
    label: Optional[str] = None
    # The unit label for this usage counter.
    unit: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageCounterLine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageCounterLine
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageCounterLine()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "unit": lambda n : setattr(self, 'unit', n.get_str_value()),
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
        writer.write_str_value("key", self.key)
        writer.write_str_value("label", self.label)
        writer.write_str_value("unit", self.unit)
        writer.write_additional_data_value(self.additional_data)
    

