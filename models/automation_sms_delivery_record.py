from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_sms_delivery_record_status import AutomationSmsDeliveryRecord_status

@dataclass
class AutomationSmsDeliveryRecord(AdditionalDataHolder, Parsable):
    """
    Delivery outcome of the persisted SMS. Workflow steps advance on command acceptance, without waiting for delivery.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Machine-readable delivery failure code.
    error_code: Optional[str] = None
    # UTC time of the next automatic delivery retry, if any.
    next_retry_at: Optional[datetime.datetime] = None
    # Redacted reason supplied by the delivery pipeline.
    reason: Optional[str] = None
    # UTC time at which the SMS is scheduled to send.
    scheduled_for: Optional[datetime.datetime] = None
    # Durable SMS event ID used to read subsequent delivery outcomes.
    sms_event_id: Optional[str] = None
    # Describes the normalized lifecycle of an SMS or MMS message from scheduling through delivery or failure.
    status: Optional[AutomationSmsDeliveryRecord_status] = None
    # Customer-safe delivery summary and suggested next action.
    summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationSmsDeliveryRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationSmsDeliveryRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationSmsDeliveryRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_sms_delivery_record_status import AutomationSmsDeliveryRecord_status

        from .automation_sms_delivery_record_status import AutomationSmsDeliveryRecord_status

        fields: dict[str, Callable[[Any], None]] = {
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "nextRetryAt": lambda n : setattr(self, 'next_retry_at', n.get_datetime_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "scheduledFor": lambda n : setattr(self, 'scheduled_for', n.get_datetime_value()),
            "smsEventId": lambda n : setattr(self, 'sms_event_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AutomationSmsDeliveryRecord_status)),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
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
        writer.write_str_value("errorCode", self.error_code)
        writer.write_datetime_value("nextRetryAt", self.next_retry_at)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("scheduledFor", self.scheduled_for)
        writer.write_str_value("smsEventId", self.sms_event_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    

