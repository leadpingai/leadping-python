from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_warmup_call_status import PhoneNumberWarmupCallStatus

@dataclass
class PhoneNumberWarmupCallResponse(AdditionalDataHolder, Parsable):
    """
    API response containing a voice call warmup attempt.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The answeredAt property
    answered_at: Optional[datetime.datetime] = None
    # The completedAt property
    completed_at: Optional[datetime.datetime] = None
    # The destinationPhoneNumber property
    destination_phone_number: Optional[str] = None
    # The destinationPhoneNumberId property
    destination_phone_number_id: Optional[str] = None
    # The failureReason property
    failure_reason: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The scheduledAt property
    scheduled_at: Optional[datetime.datetime] = None
    # The sourcePhoneNumber property
    source_phone_number: Optional[str] = None
    # The sourcePhoneNumberId property
    source_phone_number_id: Optional[str] = None
    # Defines the durable state machine statuses for voice call warmup attempts.
    status: Optional[PhoneNumberWarmupCallStatus] = None
    # The targetDurationSeconds property
    target_duration_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberWarmupCallResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberWarmupCallResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberWarmupCallResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_warmup_call_status import PhoneNumberWarmupCallStatus

        from .phone_number_warmup_call_status import PhoneNumberWarmupCallStatus

        fields: dict[str, Callable[[Any], None]] = {
            "answeredAt": lambda n : setattr(self, 'answered_at', n.get_datetime_value()),
            "completedAt": lambda n : setattr(self, 'completed_at', n.get_datetime_value()),
            "destinationPhoneNumber": lambda n : setattr(self, 'destination_phone_number', n.get_str_value()),
            "destinationPhoneNumberId": lambda n : setattr(self, 'destination_phone_number_id', n.get_str_value()),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "scheduledAt": lambda n : setattr(self, 'scheduled_at', n.get_datetime_value()),
            "sourcePhoneNumber": lambda n : setattr(self, 'source_phone_number', n.get_str_value()),
            "sourcePhoneNumberId": lambda n : setattr(self, 'source_phone_number_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PhoneNumberWarmupCallStatus)),
            "targetDurationSeconds": lambda n : setattr(self, 'target_duration_seconds', n.get_int_value()),
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
        writer.write_datetime_value("answeredAt", self.answered_at)
        writer.write_datetime_value("completedAt", self.completed_at)
        writer.write_str_value("destinationPhoneNumber", self.destination_phone_number)
        writer.write_str_value("destinationPhoneNumberId", self.destination_phone_number_id)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("scheduledAt", self.scheduled_at)
        writer.write_str_value("sourcePhoneNumber", self.source_phone_number)
        writer.write_str_value("sourcePhoneNumberId", self.source_phone_number_id)
        writer.write_enum_value("status", self.status)
        writer.write_int_value("targetDurationSeconds", self.target_duration_seconds)
        writer.write_additional_data_value(self.additional_data)
    

