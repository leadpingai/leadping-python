from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sms_warmup_action_status import SmsWarmupActionStatus
    from .sms_warmup_action_type import SmsWarmupActionType

@dataclass
class SmsWarmupActionResponse(AdditionalDataHolder, Parsable):
    """
    API response containing SMS warmup action data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action type classification for this SMS warmup action.
    action_type: Optional[SmsWarmupActionType] = None
    # The body value for this SMS warmup action.
    body: Optional[str] = None
    # The conversation ID associated with this SMS warmup action.
    conversation_id: Optional[str] = None
    # The date and time for the executed at value on this SMS warmup action.
    executed_at: Optional[datetime.datetime] = None
    # The human-readable failure reason explaining this SMS warmup action.
    failure_reason: Optional[str] = None
    # The phone number associated with this SMS warmup action.
    from_phone_number: Optional[str] = None
    # The unique ID for this SMS warmup action.
    id: Optional[str] = None
    # The date and time for the scheduled at value on this SMS warmup action.
    scheduled_at: Optional[datetime.datetime] = None
    # The current status for this SMS warmup action.
    status: Optional[SmsWarmupActionStatus] = None
    # The phone number associated with this SMS warmup action.
    to_phone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmsWarmupActionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsWarmupActionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmsWarmupActionResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sms_warmup_action_status import SmsWarmupActionStatus
        from .sms_warmup_action_type import SmsWarmupActionType

        from .sms_warmup_action_status import SmsWarmupActionStatus
        from .sms_warmup_action_type import SmsWarmupActionType

        fields: dict[str, Callable[[Any], None]] = {
            "actionType": lambda n : setattr(self, 'action_type', n.get_enum_value(SmsWarmupActionType)),
            "body": lambda n : setattr(self, 'body', n.get_str_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "executedAt": lambda n : setattr(self, 'executed_at', n.get_datetime_value()),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "scheduledAt": lambda n : setattr(self, 'scheduled_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SmsWarmupActionStatus)),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
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
        writer.write_enum_value("actionType", self.action_type)
        writer.write_str_value("body", self.body)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_datetime_value("executedAt", self.executed_at)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("scheduledAt", self.scheduled_at)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_additional_data_value(self.additional_data)
    

