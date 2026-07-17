from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_comparison import AnalyticsComparison
    from .analytics_trend_point_ofint import AnalyticsTrendPointOfint

@dataclass
class CustomerLeadTrend(AdditionalDataHolder, Parsable):
    """
    Represents customer lead trend data exposed by Leadping analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Date and time when this Leadping customer lead trend was comparison.
    comparison: Optional[AnalyticsComparison] = None
    # Collection of points included with this Leadping customer lead trend.
    points: Optional[list[AnalyticsTrendPointOfint]] = None
    # Total number of total records represented by this Leadping customer lead trend.
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerLeadTrend:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerLeadTrend
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerLeadTrend()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_comparison import AnalyticsComparison
        from .analytics_trend_point_ofint import AnalyticsTrendPointOfint

        from .analytics_comparison import AnalyticsComparison
        from .analytics_trend_point_ofint import AnalyticsTrendPointOfint

        fields: dict[str, Callable[[Any], None]] = {
            "comparison": lambda n : setattr(self, 'comparison', n.get_object_value(AnalyticsComparison)),
            "points": lambda n : setattr(self, 'points', n.get_collection_of_object_values(AnalyticsTrendPointOfint)),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        writer.write_object_value("comparison", self.comparison)
        writer.write_collection_of_object_values("points", self.points)
        writer.write_int_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

