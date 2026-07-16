from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SendSmsRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API SMS send request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Messaging campaign identifier associated with this SMS send request.
    campaign_id: Optional[str] = None
    # Conversation ID that links this SMS send request to the Leadping inbox thread.
    conversation_id: Optional[str] = None
    # Sender phone number ID used for this outbound SMS or call.
    from_phone_number_id: Optional[str] = None
    # Idempotency key used to prevent duplicate outbound delivery.
    outbound_idempotency_key: Optional[str] = None
    # UTC timestamp when Leadping should send the SMS message.
    scheduled_for: Optional[datetime.datetime] = None
    # Existing SMS event ID to reuse or update when retrying a send request.
    sms_event_id: Optional[str] = None
    # Lead source ID used for attribution and sender selection.
    source_id: Optional[str] = None
    # Body text for the SMS message or communication represented by this SMS send request.
    text: Optional[str] = None
    # Indicates whether a user manually overrode Leadping's automatic number selection for this SMS send request.
    was_manually_overridden: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SendSmsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendSmsRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SendSmsRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "outboundIdempotencyKey": lambda n : setattr(self, 'outbound_idempotency_key', n.get_str_value()),
            "scheduledFor": lambda n : setattr(self, 'scheduled_for', n.get_datetime_value()),
            "smsEventId": lambda n : setattr(self, 'sms_event_id', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "wasManuallyOverridden": lambda n : setattr(self, 'was_manually_overridden', n.get_bool_value()),
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
        writer.write_str_value("campaignId", self.campaign_id)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_str_value("outboundIdempotencyKey", self.outbound_idempotency_key)
        writer.write_datetime_value("scheduledFor", self.scheduled_for)
        writer.write_str_value("smsEventId", self.sms_event_id)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("text", self.text)
        writer.write_bool_value("wasManuallyOverridden", self.was_manually_overridden)
        writer.write_additional_data_value(self.additional_data)
    

