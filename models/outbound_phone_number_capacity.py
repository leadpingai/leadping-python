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
    # Human-readable reason for the current phone-number health state.
    health_reason: Optional[str] = None
    # Current health status for this Leadping outbound phone number capacity.
    health_status: Optional[PhoneNumberOutboundHealthStatus] = None
    # Phone number associated with this Leadping outbound phone number capacity.
    phone_number: Optional[str] = None
    # Unique identifier of the phone number associated with this Leadping outbound phone number capacity.
    phone_number_id: Optional[str] = None
    # Indicates whether this phone number has an approved 10DLC messaging campaign assignment.
    sms_approved: Optional[bool] = None
    # Next midnight Eastern time, when SMS daily capacity resets.
    sms_daily_resets_at: Optional[datetime.datetime] = None
    # Start of the next Eastern time hour, when SMS hourly capacity resets.
    sms_hourly_resets_at: Optional[datetime.datetime] = None
    # The next time SMS capacity becomes available in the rolling minute window.
    sms_minutely_resets_at: Optional[datetime.datetime] = None
    # Indicates whether SMS limits for this phone number are still ramping up.
    sms_ramping: Optional[bool] = None
    # Next midnight Eastern time, when voice daily capacity resets.
    voice_daily_resets_at: Optional[datetime.datetime] = None
    # Start of the next Eastern time hour, when voice hourly capacity resets.
    voice_hourly_resets_at: Optional[datetime.datetime] = None
    # The next time voice capacity becomes available in the rolling minute window.
    voice_minutely_resets_at: Optional[datetime.datetime] = None
    # Indicates whether call limits for this phone number are still ramping up.
    voice_ramping: Optional[bool] = None
    
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
            "healthReason": lambda n : setattr(self, 'health_reason', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(PhoneNumberOutboundHealthStatus)),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "smsApproved": lambda n : setattr(self, 'sms_approved', n.get_bool_value()),
            "smsDailyResetsAt": lambda n : setattr(self, 'sms_daily_resets_at', n.get_datetime_value()),
            "smsHourlyResetsAt": lambda n : setattr(self, 'sms_hourly_resets_at', n.get_datetime_value()),
            "smsMinutelyResetsAt": lambda n : setattr(self, 'sms_minutely_resets_at', n.get_datetime_value()),
            "smsRamping": lambda n : setattr(self, 'sms_ramping', n.get_bool_value()),
            "voiceDailyResetsAt": lambda n : setattr(self, 'voice_daily_resets_at', n.get_datetime_value()),
            "voiceHourlyResetsAt": lambda n : setattr(self, 'voice_hourly_resets_at', n.get_datetime_value()),
            "voiceMinutelyResetsAt": lambda n : setattr(self, 'voice_minutely_resets_at', n.get_datetime_value()),
            "voiceRamping": lambda n : setattr(self, 'voice_ramping', n.get_bool_value()),
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
        writer.write_str_value("healthReason", self.health_reason)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_bool_value("smsApproved", self.sms_approved)
        writer.write_datetime_value("smsDailyResetsAt", self.sms_daily_resets_at)
        writer.write_datetime_value("smsHourlyResetsAt", self.sms_hourly_resets_at)
        writer.write_datetime_value("smsMinutelyResetsAt", self.sms_minutely_resets_at)
        writer.write_bool_value("smsRamping", self.sms_ramping)
        writer.write_datetime_value("voiceDailyResetsAt", self.voice_daily_resets_at)
        writer.write_datetime_value("voiceHourlyResetsAt", self.voice_hourly_resets_at)
        writer.write_datetime_value("voiceMinutelyResetsAt", self.voice_minutely_resets_at)
        writer.write_bool_value("voiceRamping", self.voice_ramping)
        writer.write_additional_data_value(self.additional_data)
    

