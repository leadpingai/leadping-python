from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_trend_point_ofdecimal import AnalyticsTrendPointOfdecimal

@dataclass
class CustomerResponseMetrics(AdditionalDataHolder, Parsable):
    """
    Represents customer response metrics data exposed by Leadping analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of average minutes trend included with this Leadping customer response metrics.
    average_minutes_trend: Optional[list[AnalyticsTrendPointOfdecimal]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerResponseMetrics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerResponseMetrics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerResponseMetrics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_trend_point_ofdecimal import AnalyticsTrendPointOfdecimal

        from .analytics_trend_point_ofdecimal import AnalyticsTrendPointOfdecimal

        fields: dict[str, Callable[[Any], None]] = {
            "averageMinutesTrend": lambda n : setattr(self, 'average_minutes_trend', n.get_collection_of_object_values(AnalyticsTrendPointOfdecimal)),
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
        writer.write_collection_of_object_values("averageMinutesTrend", self.average_minutes_trend)
        writer.write_additional_data_value(self.additional_data)
    

