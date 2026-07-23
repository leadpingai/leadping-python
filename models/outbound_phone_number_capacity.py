from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_outbound_health_status import PhoneNumberOutboundHealthStatus

@dataclass
class OutboundPhoneNumberCapacity(AdditionalDataHolder, Parsable):
    """
    Represents outbound phone number capacity data used by Leadping.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether Leadping successfully calculated capacity for this phone number.
    capacity_available: Optional[bool] = None
    # Current health status for this Leadping outbound phone number capacity.
    health_status: Optional[PhoneNumberOutboundHealthStatus] = None
    # Phone number associated with this Leadping outbound phone number capacity.
    phone_number: Optional[str] = None
    # Unique identifier of the phone number associated with this Leadping outbound phone number capacity.
    phone_number_id: Optional[str] = None
    # Next midnight Eastern time, when SMS daily capacity resets.
    sms_daily_resets_at: Optional[datetime.datetime] = None
    # Start of the next Eastern time hour, when SMS hourly capacity resets.
    sms_hourly_resets_at: Optional[datetime.datetime] = None
    # Number of SMS limit this hour represented by this Leadping outbound phone number capacity.
    sms_limit_this_hour: Optional[int] = None
    # Number of SMS limit today represented by this Leadping outbound phone number capacity.
    sms_limit_today: Optional[int] = None
    # SMS remaining this hour for the applicable messaging or voice capacity window.
    sms_remaining_this_hour: Optional[int] = None
    # SMS remaining today for the applicable messaging or voice capacity window.
    sms_remaining_today: Optional[int] = None
    # SMS used this hour for the applicable messaging or voice capacity window.
    sms_used_this_hour: Optional[int] = None
    # SMS used today for the applicable messaging or voice capacity window.
    sms_used_today: Optional[int] = None
    # Next midnight Eastern time, when voice daily capacity resets.
    voice_daily_resets_at: Optional[datetime.datetime] = None
    # Start of the next Eastern time hour, when voice hourly capacity resets.
    voice_hourly_resets_at: Optional[datetime.datetime] = None
    # Voice limit this hour associated with this Leadping outbound phone number capacity.
    voice_limit_this_hour: Optional[int] = None
    # Voice limit today associated with this Leadping outbound phone number capacity.
    voice_limit_today: Optional[int] = None
    # Voice remaining this hour for the applicable messaging or voice capacity window.
    voice_remaining_this_hour: Optional[int] = None
    # Voice remaining today for the applicable messaging or voice capacity window.
    voice_remaining_today: Optional[int] = None
    # Voice used this hour for the applicable messaging or voice capacity window.
    voice_used_this_hour: Optional[int] = None
    # Voice used today for the applicable messaging or voice capacity window.
    voice_used_today: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutboundPhoneNumberCapacity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutboundPhoneNumberCapacity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutboundPhoneNumberCapacity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_outbound_health_status import PhoneNumberOutboundHealthStatus

        from .phone_number_outbound_health_status import PhoneNumberOutboundHealthStatus

        fields: dict[str, Callable[[Any], None]] = {
            "capacityAvailable": lambda n : setattr(self, 'capacity_available', n.get_bool_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(PhoneNumberOutboundHealthStatus)),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "smsDailyResetsAt": lambda n : setattr(self, 'sms_daily_resets_at', n.get_datetime_value()),
            "smsHourlyResetsAt": lambda n : setattr(self, 'sms_hourly_resets_at', n.get_datetime_value()),
            "smsLimitThisHour": lambda n : setattr(self, 'sms_limit_this_hour', n.get_int_value()),
            "smsLimitToday": lambda n : setattr(self, 'sms_limit_today', n.get_int_value()),
            "smsRemainingThisHour": lambda n : setattr(self, 'sms_remaining_this_hour', n.get_int_value()),
            "smsRemainingToday": lambda n : setattr(self, 'sms_remaining_today', n.get_int_value()),
            "smsUsedThisHour": lambda n : setattr(self, 'sms_used_this_hour', n.get_int_value()),
            "smsUsedToday": lambda n : setattr(self, 'sms_used_today', n.get_int_value()),
            "voiceDailyResetsAt": lambda n : setattr(self, 'voice_daily_resets_at', n.get_datetime_value()),
            "voiceHourlyResetsAt": lambda n : setattr(self, 'voice_hourly_resets_at', n.get_datetime_value()),
            "voiceLimitThisHour": lambda n : setattr(self, 'voice_limit_this_hour', n.get_int_value()),
            "voiceLimitToday": lambda n : setattr(self, 'voice_limit_today', n.get_int_value()),
            "voiceRemainingThisHour": lambda n : setattr(self, 'voice_remaining_this_hour', n.get_int_value()),
            "voiceRemainingToday": lambda n : setattr(self, 'voice_remaining_today', n.get_int_value()),
            "voiceUsedThisHour": lambda n : setattr(self, 'voice_used_this_hour', n.get_int_value()),
            "voiceUsedToday": lambda n : setattr(self, 'voice_used_today', n.get_int_value()),
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
        writer.write_bool_value("capacityAvailable", self.capacity_available)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_datetime_value("smsDailyResetsAt", self.sms_daily_resets_at)
        writer.write_datetime_value("smsHourlyResetsAt", self.sms_hourly_resets_at)
        writer.write_int_value("smsLimitThisHour", self.sms_limit_this_hour)
        writer.write_int_value("smsLimitToday", self.sms_limit_today)
        writer.write_int_value("smsRemainingThisHour", self.sms_remaining_this_hour)
        writer.write_int_value("smsRemainingToday", self.sms_remaining_today)
        writer.write_int_value("smsUsedThisHour", self.sms_used_this_hour)
        writer.write_int_value("smsUsedToday", self.sms_used_today)
        writer.write_datetime_value("voiceDailyResetsAt", self.voice_daily_resets_at)
        writer.write_datetime_value("voiceHourlyResetsAt", self.voice_hourly_resets_at)
        writer.write_int_value("voiceLimitThisHour", self.voice_limit_this_hour)
        writer.write_int_value("voiceLimitToday", self.voice_limit_today)
        writer.write_int_value("voiceRemainingThisHour", self.voice_remaining_this_hour)
        writer.write_int_value("voiceRemainingToday", self.voice_remaining_today)
        writer.write_int_value("voiceUsedThisHour", self.voice_used_this_hour)
        writer.write_int_value("voiceUsedToday", self.voice_used_today)
        writer.write_additional_data_value(self.additional_data)
    

