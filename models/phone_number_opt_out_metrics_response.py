from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneNumberOptOutMetricsResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API phone number opt-out metrics response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Number of distinct recipients contacted during this metrics window.
    distinct_contacted_count: Optional[int] = None
    # Number of recipients who opted out during this metrics window.
    opt_out_count: Optional[int] = None
    # Percentage of contacted recipients who opted out during this metrics window.
    opt_out_rate_percent: Optional[float] = None
    # Number of days included in the metrics reporting window.
    window_days: Optional[int] = None
    # UTC timestamp when the metrics reporting window starts.
    window_started_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberOptOutMetricsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberOptOutMetricsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberOptOutMetricsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "distinctContactedCount": lambda n : setattr(self, 'distinct_contacted_count', n.get_int_value()),
            "optOutCount": lambda n : setattr(self, 'opt_out_count', n.get_int_value()),
            "optOutRatePercent": lambda n : setattr(self, 'opt_out_rate_percent', n.get_float_value()),
            "windowDays": lambda n : setattr(self, 'window_days', n.get_int_value()),
            "windowStartedAt": lambda n : setattr(self, 'window_started_at', n.get_datetime_value()),
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
        writer.write_int_value("distinctContactedCount", self.distinct_contacted_count)
        writer.write_int_value("optOutCount", self.opt_out_count)
        writer.write_float_value("optOutRatePercent", self.opt_out_rate_percent)
        writer.write_int_value("windowDays", self.window_days)
        writer.write_datetime_value("windowStartedAt", self.window_started_at)
        writer.write_additional_data_value(self.additional_data)
    

