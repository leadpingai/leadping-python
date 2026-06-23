from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sms_warmup_action_response import SmsWarmupActionResponse
    from .sms_warmup_health_state import SmsWarmupHealthState
    from .sms_warmup_ui_state import SmsWarmupUiState

@dataclass
class SmsWarmupStatusResponse(AdditionalDataHolder, Parsable):
    """
    API response containing SMS warmup status data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The human-readable block reason explaining this SMS warmup status.
    block_reason: Optional[str] = None
    # Whether the caller can pause this SMS warmup status.
    can_pause: Optional[bool] = None
    # Whether the caller can resume this SMS warmup status.
    can_resume: Optional[bool] = None
    # The carrier rejection count for this SMS warmup status.
    carrier_rejection_count: Optional[int] = None
    # The date and time for the completed at value on this SMS warmup status.
    completed_at: Optional[datetime.datetime] = None
    # The delivered count for this SMS warmup status.
    delivered_count: Optional[int] = None
    # The delivery success rate metric for this SMS warmup status.
    delivery_success_rate: Optional[float] = None
    # The failure count for this SMS warmup status.
    failure_count: Optional[int] = None
    # Whether global warmup is enabled for this SMS warmup status.
    global_warmup_enabled: Optional[bool] = None
    # The health score metric for this SMS warmup status.
    health_score: Optional[int] = None
    # Whether this SMS warmup status is approved test destination.
    is_approved_test_destination: Optional[bool] = None
    # Whether this SMS warmup status is internal pool.
    is_internal_pool: Optional[bool] = None
    # Whether this SMS warmup status is messaging program approved.
    is_messaging_program_approved: Optional[bool] = None
    # The date and time for the last health snapshot at value on this SMS warmup status.
    last_health_snapshot_at: Optional[datetime.datetime] = None
    # The date and time for the last successful message at value on this SMS warmup status.
    last_successful_message_at: Optional[datetime.datetime] = None
    # The date and time for the next scheduled action at value on this SMS warmup status.
    next_scheduled_action_at: Optional[datetime.datetime] = None
    # The opt out signal count for this SMS warmup status.
    opt_out_signal_count: Optional[int] = None
    # The human-readable pause reason explaining this SMS warmup status.
    pause_reason: Optional[str] = None
    # The phone number associated with this SMS warmup status.
    phone_number: Optional[str] = None
    # The phone number ID associated with this SMS warmup status.
    phone_number_id: Optional[str] = None
    # The progress percent metric for this SMS warmup status.
    progress_percent: Optional[int] = None
    # The received count for this SMS warmup status.
    received_count: Optional[int] = None
    # The recent actions included with this SMS warmup status.
    recent_actions: Optional[list[SmsWarmupActionResponse]] = None
    # The sent count for this SMS warmup status.
    sent_count: Optional[int] = None
    # The spam signal count for this SMS warmup status.
    spam_signal_count: Optional[int] = None
    # The date and time for the started at value on this SMS warmup status.
    started_at: Optional[datetime.datetime] = None
    # The current status for this SMS warmup status.
    status: Optional[SmsWarmupHealthState] = None
    # The current UI state for this SMS warmup status.
    ui_state: Optional[SmsWarmupUiState] = None
    # Whether warmup is enabled for this SMS warmup status.
    warmup_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmsWarmupStatusResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsWarmupStatusResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmsWarmupStatusResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sms_warmup_action_response import SmsWarmupActionResponse
        from .sms_warmup_health_state import SmsWarmupHealthState
        from .sms_warmup_ui_state import SmsWarmupUiState

        from .sms_warmup_action_response import SmsWarmupActionResponse
        from .sms_warmup_health_state import SmsWarmupHealthState
        from .sms_warmup_ui_state import SmsWarmupUiState

        fields: dict[str, Callable[[Any], None]] = {
            "blockReason": lambda n : setattr(self, 'block_reason', n.get_str_value()),
            "canPause": lambda n : setattr(self, 'can_pause', n.get_bool_value()),
            "canResume": lambda n : setattr(self, 'can_resume', n.get_bool_value()),
            "carrierRejectionCount": lambda n : setattr(self, 'carrier_rejection_count', n.get_int_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "deliveredCount": lambda n : setattr(self, 'delivered_count', n.get_int_value()),
            "deliverySuccessRate": lambda n : setattr(self, 'delivery_success_rate', n.get_float_value()),
            "failureCount": lambda n : setattr(self, 'failure_count', n.get_int_value()),
            "globalWarmupEnabled": lambda n : setattr(self, 'global_warmup_enabled', n.get_bool_value()),
            "healthScore": lambda n : setattr(self, 'health_score', n.get_int_value()),
            "isApprovedTestDestination": lambda n : setattr(self, 'is_approved_test_destination', n.get_bool_value()),
            "isInternalPool": lambda n : setattr(self, 'is_internal_pool', n.get_bool_value()),
            "isMessagingProgramApproved": lambda n : setattr(self, 'is_messaging_program_approved', n.get_bool_value()),
            "lastHealthSnapshotAt": lambda n : setattr(self, 'last_health_snapshot_at', n.get_datetime_value()),
            "lastSuccessfulMessageAt": lambda n : setattr(self, 'last_successful_message_at', n.get_datetime_value()),
            "nextScheduledActionAt": lambda n : setattr(self, 'next_scheduled_action_at', n.get_datetime_value()),
            "optOutSignalCount": lambda n : setattr(self, 'opt_out_signal_count', n.get_int_value()),
            "pauseReason": lambda n : setattr(self, 'pause_reason', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "progressPercent": lambda n : setattr(self, 'progress_percent', n.get_int_value()),
            "receivedCount": lambda n : setattr(self, 'received_count', n.get_int_value()),
            "recentActions": lambda n : setattr(self, 'recent_actions', n.get_collection_of_object_values(SmsWarmupActionResponse)),
            "sentCount": lambda n : setattr(self, 'sent_count', n.get_int_value()),
            "spamSignalCount": lambda n : setattr(self, 'spam_signal_count', n.get_int_value()),
            "startedAt": lambda n : setattr(self, 'started_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SmsWarmupHealthState)),
            "uiState": lambda n : setattr(self, 'ui_state', n.get_object_value(SmsWarmupUiState)),
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
        writer.write_str_value("blockReason", self.block_reason)
        writer.write_bool_value("canPause", self.can_pause)
        writer.write_bool_value("canResume", self.can_resume)
        writer.write_int_value("carrierRejectionCount", self.carrier_rejection_count)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_int_value("deliveredCount", self.delivered_count)
        writer.write_float_value("deliverySuccessRate", self.delivery_success_rate)
        writer.write_int_value("failureCount", self.failure_count)
        writer.write_bool_value("globalWarmupEnabled", self.global_warmup_enabled)
        writer.write_int_value("healthScore", self.health_score)
        writer.write_bool_value("isApprovedTestDestination", self.is_approved_test_destination)
        writer.write_bool_value("isInternalPool", self.is_internal_pool)
        writer.write_bool_value("isMessagingProgramApproved", self.is_messaging_program_approved)
        writer.write_datetime_value("lastHealthSnapshotAt", self.last_health_snapshot_at)
        writer.write_datetime_value("lastSuccessfulMessageAt", self.last_successful_message_at)
        writer.write_datetime_value("nextScheduledActionAt", self.next_scheduled_action_at)
        writer.write_int_value("optOutSignalCount", self.opt_out_signal_count)
        writer.write_str_value("pauseReason", self.pause_reason)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_int_value("progressPercent", self.progress_percent)
        writer.write_int_value("receivedCount", self.received_count)
        writer.write_collection_of_object_values("recentActions", self.recent_actions)
        writer.write_int_value("sentCount", self.sent_count)
        writer.write_int_value("spamSignalCount", self.spam_signal_count)
        writer.write_datetime_value("startedAt", self.started_at)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("uiState", self.ui_state)
        writer.write_bool_value("warmupEnabled", self.warmup_enabled)
        writer.write_additional_data_value(self.additional_data)
    

