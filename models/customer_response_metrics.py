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
    Response metrics associated with this Leadping customer analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of average minutes trend included with this Leadping customer response metrics.
    average_minutes_trend: Optional[list[AnalyticsTrendPointOfdecimal]] = None
    # Number of calls missed during the reporting period.
    missed_calls: Optional[int] = None
    # Number of responded leads represented by this Leadping customer response metrics.
    responded_leads: Optional[int] = None
    # Responded within five minutes percent expressed as a percentage.
    responded_within_five_minutes_percent: Optional[float] = None
    # Number of unread messages represented by this Leadping customer response metrics.
    unread_messages: Optional[int] = None
    # Number of unresponded leads represented by this Leadping customer response metrics.
    unresponded_leads: Optional[int] = None
    
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
            "missedCalls": lambda n : setattr(self, 'missed_calls', n.get_int_value()),
            "respondedLeads": lambda n : setattr(self, 'responded_leads', n.get_int_value()),
            "respondedWithinFiveMinutesPercent": lambda n : setattr(self, 'responded_within_five_minutes_percent', n.get_float_value()),
            "unreadMessages": lambda n : setattr(self, 'unread_messages', n.get_int_value()),
            "unrespondedLeads": lambda n : setattr(self, 'unresponded_leads', n.get_int_value()),
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
        writer.write_int_value("missedCalls", self.missed_calls)
        writer.write_int_value("respondedLeads", self.responded_leads)
        writer.write_float_value("respondedWithinFiveMinutesPercent", self.responded_within_five_minutes_percent)
        writer.write_int_value("unreadMessages", self.unread_messages)
        writer.write_int_value("unrespondedLeads", self.unresponded_leads)
        writer.write_additional_data_value(self.additional_data)
    

