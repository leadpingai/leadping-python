from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AnalyticsComparison(AdditionalDataHolder, Parsable):
    """
    Date and time when this Leadping customer analytics summary was leads comparison.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Metric value for the current reporting period.
    current: Optional[float] = None
    # Direction classification for this Leadping analytics comparison.
    direction: Optional[str] = None
    # Metric value for the preceding comparison period.
    previous: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyticsComparison:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyticsComparison
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyticsComparison()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "current": lambda n : setattr(self, 'current', n.get_float_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "previous": lambda n : setattr(self, 'previous', n.get_float_value()),
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
        writer.write_float_value("current", self.current)
        writer.write_str_value("direction", self.direction)
        writer.write_float_value("previous", self.previous)
        writer.write_additional_data_value(self.additional_data)
    

