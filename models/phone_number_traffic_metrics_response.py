from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_traffic_trend_point import PhoneNumberTrafficTrendPoint

@dataclass
class PhoneNumberTrafficMetricsResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API phone number traffic metrics response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Number of outbound calls that connected during this metrics window.
    call_connected_count: Optional[int] = None
    # Number of outbound calls that failed during this metrics window.
    call_failed_count: Optional[int] = None
    # Number of outbound calls that failed because the destination number was invalid during this metrics window.
    call_invalid_number_count: Optional[int] = None
    # Number of outbound calls placed during this metrics window.
    call_placed_count: Optional[int] = None
    # Number of connected outbound calls shorter than 30 seconds during this metrics window.
    call_short_count: Optional[int] = None
    # Number of SMS messages that failed during this metrics window.
    sms_failed_count: Optional[int] = None
    # Number of SMS messages sent during this metrics window.
    sms_sent_count: Optional[int] = None
    # Time-series buckets that show how the metric changes across the reporting window.
    trend: Optional[list[PhoneNumberTrafficTrendPoint]] = None
    # Number of days included in the metrics reporting window.
    window_days: Optional[int] = None
    # UTC timestamp when the metrics reporting window starts.
    window_started_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberTrafficMetricsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberTrafficMetricsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberTrafficMetricsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_traffic_trend_point import PhoneNumberTrafficTrendPoint

        from .phone_number_traffic_trend_point import PhoneNumberTrafficTrendPoint

        fields: dict[str, Callable[[Any], None]] = {
            "callConnectedCount": lambda n : setattr(self, 'call_connected_count', n.get_int_value()),
            "callFailedCount": lambda n : setattr(self, 'call_failed_count', n.get_int_value()),
            "callInvalidNumberCount": lambda n : setattr(self, 'call_invalid_number_count', n.get_int_value()),
            "callPlacedCount": lambda n : setattr(self, 'call_placed_count', n.get_int_value()),
            "callShortCount": lambda n : setattr(self, 'call_short_count', n.get_int_value()),
            "smsFailedCount": lambda n : setattr(self, 'sms_failed_count', n.get_int_value()),
            "smsSentCount": lambda n : setattr(self, 'sms_sent_count', n.get_int_value()),
            "trend": lambda n : setattr(self, 'trend', n.get_collection_of_object_values(PhoneNumberTrafficTrendPoint)),
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
        writer.write_int_value("callConnectedCount", self.call_connected_count)
        writer.write_int_value("callFailedCount", self.call_failed_count)
        writer.write_int_value("callInvalidNumberCount", self.call_invalid_number_count)
        writer.write_int_value("callPlacedCount", self.call_placed_count)
        writer.write_int_value("callShortCount", self.call_short_count)
        writer.write_int_value("smsFailedCount", self.sms_failed_count)
        writer.write_int_value("smsSentCount", self.sms_sent_count)
        writer.write_collection_of_object_values("trend", self.trend)
        writer.write_int_value("windowDays", self.window_days)
        writer.write_datetime_value("windowStartedAt", self.window_started_at)
        writer.write_additional_data_value(self.additional_data)
    

