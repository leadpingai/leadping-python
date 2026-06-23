from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_warmup_call_response import PhoneNumberWarmupCallResponse
    from .phone_number_warmup_health_status import PhoneNumberWarmupHealthStatus
    from .phone_number_warmup_stage import PhoneNumberWarmupStage

@dataclass
class PhoneNumberWarmupStatusResponse(AdditionalDataHolder, Parsable):
    """
    API response containing voice call warmup status for a Leadping-managed phone number.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The callsThisHour property
    calls_this_hour: Optional[int] = None
    # The callsToday property
    calls_today: Optional[int] = None
    # The completedAt property
    completed_at: Optional[datetime.datetime] = None
    # The consecutiveFailedCalls property
    consecutive_failed_calls: Optional[int] = None
    # The consecutiveSuccessfulCalls property
    consecutive_successful_calls: Optional[int] = None
    # The dailyCap property
    daily_cap: Optional[int] = None
    # The failureReason property
    failure_reason: Optional[str] = None
    # The hourlyCap property
    hourly_cap: Optional[int] = None
    # The lastSuccessfulWarmupAt property
    last_successful_warmup_at: Optional[datetime.datetime] = None
    # The lowConfidenceTimeZone property
    low_confidence_time_zone: Optional[bool] = None
    # The maxTargetDurationSeconds property
    max_target_duration_seconds: Optional[int] = None
    # The minTargetDurationSeconds property
    min_target_duration_seconds: Optional[int] = None
    # The networkWarmupOptIn property
    network_warmup_opt_in: Optional[bool] = None
    # The nextEligibleAt property
    next_eligible_at: Optional[datetime.datetime] = None
    # The phoneNumber property
    phone_number: Optional[str] = None
    # The phoneNumberId property
    phone_number_id: Optional[str] = None
    # The recentCalls property
    recent_calls: Optional[list[PhoneNumberWarmupCallResponse]] = None
    # Defines the supported voice call warmup stages for a Leadping-managed phone number.
    stage: Optional[PhoneNumberWarmupStage] = None
    # The startAt property
    start_at: Optional[datetime.datetime] = None
    # Defines the supported health states for controlled internal voice call warmup.
    status: Optional[PhoneNumberWarmupHealthStatus] = None
    # The timeZoneId property
    time_zone_id: Optional[str] = None
    # The totalFailedCalls property
    total_failed_calls: Optional[int] = None
    # The totalSuccessfulCalls property
    total_successful_calls: Optional[int] = None
    # The warmupEnabled property
    warmup_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberWarmupStatusResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberWarmupStatusResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberWarmupStatusResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_warmup_call_response import PhoneNumberWarmupCallResponse
        from .phone_number_warmup_health_status import PhoneNumberWarmupHealthStatus
        from .phone_number_warmup_stage import PhoneNumberWarmupStage

        from .phone_number_warmup_call_response import PhoneNumberWarmupCallResponse
        from .phone_number_warmup_health_status import PhoneNumberWarmupHealthStatus
        from .phone_number_warmup_stage import PhoneNumberWarmupStage

        fields: dict[str, Callable[[Any], None]] = {
            "callsThisHour": lambda n : setattr(self, 'calls_this_hour', n.get_int_value()),
            "callsToday": lambda n : setattr(self, 'calls_today', n.get_int_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "consecutiveFailedCalls": lambda n : setattr(self, 'consecutive_failed_calls', n.get_int_value()),
            "consecutiveSuccessfulCalls": lambda n : setattr(self, 'consecutive_successful_calls', n.get_int_value()),
            "dailyCap": lambda n : setattr(self, 'daily_cap', n.get_int_value()),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "hourlyCap": lambda n : setattr(self, 'hourly_cap', n.get_int_value()),
            "lastSuccessfulWarmupAt": lambda n : setattr(self, 'last_successful_warmup_at', n.get_datetime_value()),
            "lowConfidenceTimeZone": lambda n : setattr(self, 'low_confidence_time_zone', n.get_bool_value()),
            "maxTargetDurationSeconds": lambda n : setattr(self, 'max_target_duration_seconds', n.get_int_value()),
            "minTargetDurationSeconds": lambda n : setattr(self, 'min_target_duration_seconds', n.get_int_value()),
            "networkWarmupOptIn": lambda n : setattr(self, 'network_warmup_opt_in', n.get_bool_value()),
            "nextEligibleAt": lambda n : setattr(self, 'next_eligible_at', n.get_datetime_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "recentCalls": lambda n : setattr(self, 'recent_calls', n.get_collection_of_object_values(PhoneNumberWarmupCallResponse)),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(PhoneNumberWarmupStage)),
            "startAt": lambda n : setattr(self, 'start_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PhoneNumberWarmupHealthStatus)),
            "timeZoneId": lambda n : setattr(self, 'time_zone_id', n.get_str_value()),
            "totalFailedCalls": lambda n : setattr(self, 'total_failed_calls', n.get_int_value()),
            "totalSuccessfulCalls": lambda n : setattr(self, 'total_successful_calls', n.get_int_value()),
            "warmupEnabled": lambda n : setattr(self, 'warmup_enabled', n.get_bool_value()),
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
        writer.write_int_value("callsThisHour", self.calls_this_hour)
        writer.write_int_value("callsToday", self.calls_today)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_int_value("consecutiveFailedCalls", self.consecutive_failed_calls)
        writer.write_int_value("consecutiveSuccessfulCalls", self.consecutive_successful_calls)
        writer.write_int_value("dailyCap", self.daily_cap)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_int_value("hourlyCap", self.hourly_cap)
        writer.write_datetime_value("lastSuccessfulWarmupAt", self.last_successful_warmup_at)
        writer.write_bool_value("lowConfidenceTimeZone", self.low_confidence_time_zone)
        writer.write_int_value("maxTargetDurationSeconds", self.max_target_duration_seconds)
        writer.write_int_value("minTargetDurationSeconds", self.min_target_duration_seconds)
        writer.write_bool_value("networkWarmupOptIn", self.network_warmup_opt_in)
        writer.write_datetime_value("nextEligibleAt", self.next_eligible_at)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_collection_of_object_values("recentCalls", self.recent_calls)
        writer.write_enum_value("stage", self.stage)
        writer.write_datetime_value("startAt", self.start_at)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_int_value("totalFailedCalls", self.total_failed_calls)
        writer.write_int_value("totalSuccessfulCalls", self.total_successful_calls)
        writer.write_bool_value("warmupEnabled", self.warmup_enabled)
        writer.write_additional_data_value(self.additional_data)
    

