from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .usage_counter_line import UsageCounterLine
    from .usage_summary_line import UsageSummaryLine

@dataclass
class UsageSummaryResponse(AdditionalDataHolder, Parsable):
    """
    Describes usage summary response data used by Leadping.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The named usage counters included with this usage summary.
    counters: Optional[list[UsageCounterLine]] = None
    # The lines included with this usage summary.
    lines: Optional[list[UsageSummaryLine]] = None
    # UTC timestamp for period end on this usage summary.
    period_end: Optional[datetime.datetime] = None
    # UTC timestamp for period start on this usage summary.
    period_start: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageSummaryResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageSummaryResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageSummaryResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .usage_counter_line import UsageCounterLine
        from .usage_summary_line import UsageSummaryLine

        from .usage_counter_line import UsageCounterLine
        from .usage_summary_line import UsageSummaryLine

        fields: dict[str, Callable[[Any], None]] = {
            "counters": lambda n : setattr(self, 'counters', n.get_collection_of_object_values(UsageCounterLine)),
            "lines": lambda n : setattr(self, 'lines', n.get_collection_of_object_values(UsageSummaryLine)),
            "periodEnd": lambda n : setattr(self, 'period_end', n.get_datetime_value()),
            "periodStart": lambda n : setattr(self, 'period_start', n.get_datetime_value()),
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
        writer.write_collection_of_object_values("counters", self.counters)
        writer.write_collection_of_object_values("lines", self.lines)
        writer.write_datetime_value("periodEnd", self.period_end)
        writer.write_datetime_value("periodStart", self.period_start)
        writer.write_additional_data_value(self.additional_data)
    

