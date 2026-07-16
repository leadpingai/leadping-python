from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_date_range import AnalyticsDateRange
    from .analytics_trend_point_ofint import AnalyticsTrendPointOfint

@dataclass
class SourceMetricsResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Date and time when the source metrics was generated.
    generated_at: Optional[datetime.datetime] = None
    # Collection of points included with this Leadping source metrics.
    points: Optional[list[AnalyticsTrendPointOfint]] = None
    # Range associated with this Leadping source metrics.
    range: Optional[AnalyticsDateRange] = None
    # Total number of leads records represented by this Leadping source metrics.
    total_leads: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SourceMetricsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SourceMetricsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SourceMetricsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_date_range import AnalyticsDateRange
        from .analytics_trend_point_ofint import AnalyticsTrendPointOfint

        from .analytics_date_range import AnalyticsDateRange
        from .analytics_trend_point_ofint import AnalyticsTrendPointOfint

        fields: dict[str, Callable[[Any], None]] = {
            "generatedAt": lambda n : setattr(self, 'generated_at', n.get_datetime_value()),
            "points": lambda n : setattr(self, 'points', n.get_collection_of_object_values(AnalyticsTrendPointOfint)),
            "range": lambda n : setattr(self, 'range', n.get_object_value(AnalyticsDateRange)),
            "totalLeads": lambda n : setattr(self, 'total_leads', n.get_int_value()),
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
        writer.write_datetime_value("generatedAt", self.generated_at)
        writer.write_collection_of_object_values("points", self.points)
        writer.write_object_value("range", self.range)
        writer.write_int_value("totalLeads", self.total_leads)
        writer.write_additional_data_value(self.additional_data)
    

