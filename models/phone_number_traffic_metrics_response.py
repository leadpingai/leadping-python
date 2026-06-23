from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneNumberTrafficMetricsResponse(AdditionalDataHolder, Parsable):
    """
    API response containing phone number traffic metrics data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The call failed count for this phone number traffic metrics.
    call_failed_count: Optional[int] = None
    # The call placed count for this phone number traffic metrics.
    call_placed_count: Optional[int] = None
    # The SMS failed count for this phone number traffic metrics.
    sms_failed_count: Optional[int] = None
    # The SMS sent count for this phone number traffic metrics.
    sms_sent_count: Optional[int] = None
    # The date and time for the window days value on this phone number traffic metrics.
    window_days: Optional[int] = None
    # The date and time for the window started at value on this phone number traffic metrics.
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
        fields: dict[str, Callable[[Any], None]] = {
            "callFailedCount": lambda n : setattr(self, 'call_failed_count', n.get_int_value()),
            "callPlacedCount": lambda n : setattr(self, 'call_placed_count', n.get_int_value()),
            "smsFailedCount": lambda n : setattr(self, 'sms_failed_count', n.get_int_value()),
            "smsSentCount": lambda n : setattr(self, 'sms_sent_count', n.get_int_value()),
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
        writer.write_int_value("callFailedCount", self.call_failed_count)
        writer.write_int_value("callPlacedCount", self.call_placed_count)
        writer.write_int_value("smsFailedCount", self.sms_failed_count)
        writer.write_int_value("smsSentCount", self.sms_sent_count)
        writer.write_int_value("windowDays", self.window_days)
        writer.write_datetime_value("windowStartedAt", self.window_started_at)
        writer.write_additional_data_value(self.additional_data)
    

