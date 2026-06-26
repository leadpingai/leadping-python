from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneNumberTrafficTrendPoint(AdditionalDataHolder, Parsable):
    """
    Time-series data point schema for Leadping API phone number traffic trend bucket charts and metrics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Number of outbound calls that failed during this metrics window.
    call_failed_count: Optional[int] = None
    # Number of outbound calls placed during this metrics window.
    call_placed_count: Optional[int] = None
    # UTC timestamp when this reporting bucket ends.
    end_at: Optional[datetime.datetime] = None
    # Short display label for this phone number traffic trend bucket, formatted for charts, filters, or list views.
    label: Optional[str] = None
    # Number of SMS messages that failed during this metrics window.
    sms_failed_count: Optional[int] = None
    # Number of SMS messages sent during this metrics window.
    sms_sent_count: Optional[int] = None
    # UTC timestamp when this reporting bucket starts.
    start_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberTrafficTrendPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberTrafficTrendPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberTrafficTrendPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "callFailedCount": lambda n : setattr(self, 'call_failed_count', n.get_int_value()),
            "callPlacedCount": lambda n : setattr(self, 'call_placed_count', n.get_int_value()),
            "endAt": lambda n : setattr(self, 'end_at', n.get_datetime_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "smsFailedCount": lambda n : setattr(self, 'sms_failed_count', n.get_int_value()),
            "smsSentCount": lambda n : setattr(self, 'sms_sent_count', n.get_int_value()),
            "startAt": lambda n : setattr(self, 'start_at', n.get_datetime_value()),
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
        writer.write_int_value("callFailedCount", self.call_failed_count)
        writer.write_int_value("callPlacedCount", self.call_placed_count)
        writer.write_datetime_value("endAt", self.end_at)
        writer.write_str_value("label", self.label)
        writer.write_int_value("smsFailedCount", self.sms_failed_count)
        writer.write_int_value("smsSentCount", self.sms_sent_count)
        writer.write_datetime_value("startAt", self.start_at)
        writer.write_additional_data_value(self.additional_data)
    

