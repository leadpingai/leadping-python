from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sms_warmup_health_state import SmsWarmupHealthState
    from .sms_warmup_ui_state import SmsWarmupUiState

@dataclass
class SmsWarmupStatusResponse(AdditionalDataHolder, Parsable):
    """
    API response containing SMS warmup status data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The health score metric for this SMS warmup status.
    health_score: Optional[int] = None
    # The phone number associated with this SMS warmup status.
    phone_number: Optional[str] = None
    # The phone number ID associated with this SMS warmup status.
    phone_number_id: Optional[str] = None
    # The progress percent metric for this SMS warmup status.
    progress_percent: Optional[int] = None
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
        from .sms_warmup_health_state import SmsWarmupHealthState
        from .sms_warmup_ui_state import SmsWarmupUiState

        from .sms_warmup_health_state import SmsWarmupHealthState
        from .sms_warmup_ui_state import SmsWarmupUiState

        fields: dict[str, Callable[[Any], None]] = {
            "healthScore": lambda n : setattr(self, 'health_score', n.get_int_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneNumberId": lambda n : setattr(self, 'phone_number_id', n.get_str_value()),
            "progressPercent": lambda n : setattr(self, 'progress_percent', n.get_int_value()),
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
        writer.write_int_value("healthScore", self.health_score)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("phoneNumberId", self.phone_number_id)
        writer.write_int_value("progressPercent", self.progress_percent)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("uiState", self.ui_state)
        writer.write_bool_value("warmupEnabled", self.warmup_enabled)
        writer.write_additional_data_value(self.additional_data)
    

