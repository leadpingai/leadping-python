from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .send_sms_request_outbound_priority import SendSmsRequest_outboundPriority
    from .send_sms_request_outbound_source import SendSmsRequest_outboundSource
    from .send_sms_request_selection_reason import SendSmsRequest_selectionReason

@dataclass
class SendSmsRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for send SMS.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The automation ID responsible for this SMS, if applicable.
    automation_id: Optional[str] = None
    # The campaign ID associated with this SMS.
    campaign_id: Optional[str] = None
    # The conversation ID associated with this SMS.
    conversation_id: Optional[str] = None
    # The from phone number ID associated with this SMS.
    from_phone_number_id: Optional[str] = None
    # Whether required consent is known for this outbound SMS.
    has_required_consent: Optional[bool] = None
    # The import batch ID responsible for this SMS, if applicable.
    import_batch_id: Optional[str] = None
    # Whether this SMS is automated.
    is_automated: Optional[bool] = None
    # Whether this SMS is for an imported lead.
    is_imported_lead: Optional[bool] = None
    # The outbound delivery request ID assigned by delivery control.
    outbound_delivery_request_id: Optional[str] = None
    # Optional idempotency key for retry-safe outbound delivery control.
    outbound_idempotency_key: Optional[str] = None
    # Defines priority classes used when pacing outbound delivery.
    outbound_priority: Optional[SendSmsRequest_outboundPriority] = None
    # The outbound reservation ID assigned by delivery control.
    outbound_reservation_id: Optional[str] = None
    # Defines the source that requested outbound delivery.
    outbound_source: Optional[SendSmsRequest_outboundSource] = None
    # The date and time for the scheduled for value on this SMS.
    scheduled_for: Optional[datetime.datetime] = None
    # Defines the supported Outgoing Number Selection Reason values.
    selection_reason: Optional[SendSmsRequest_selectionReason] = None
    # The SMS event ID associated with this SMS.
    sms_event_id: Optional[str] = None
    # The source ID associated with this SMS.
    source_id: Optional[str] = None
    # The text value for this SMS.
    text: Optional[str] = None
    # Whether this SMS was manually overridden.
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
        from .send_sms_request_outbound_priority import SendSmsRequest_outboundPriority
        from .send_sms_request_outbound_source import SendSmsRequest_outboundSource
        from .send_sms_request_selection_reason import SendSmsRequest_selectionReason

        from .send_sms_request_outbound_priority import SendSmsRequest_outboundPriority
        from .send_sms_request_outbound_source import SendSmsRequest_outboundSource
        from .send_sms_request_selection_reason import SendSmsRequest_selectionReason

        fields: dict[str, Callable[[Any], None]] = {
            "automationId": lambda n : setattr(self, 'automation_id', n.get_str_value()),
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "hasRequiredConsent": lambda n : setattr(self, 'has_required_consent', n.get_bool_value()),
            "importBatchId": lambda n : setattr(self, 'import_batch_id', n.get_str_value()),
            "isAutomated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "isImportedLead": lambda n : setattr(self, 'is_imported_lead', n.get_bool_value()),
            "outboundDeliveryRequestId": lambda n : setattr(self, 'outbound_delivery_request_id', n.get_str_value()),
            "outboundIdempotencyKey": lambda n : setattr(self, 'outbound_idempotency_key', n.get_str_value()),
            "outboundPriority": lambda n : setattr(self, 'outbound_priority', n.get_enum_value(SendSmsRequest_outboundPriority)),
            "outboundReservationId": lambda n : setattr(self, 'outbound_reservation_id', n.get_str_value()),
            "outboundSource": lambda n : setattr(self, 'outbound_source', n.get_enum_value(SendSmsRequest_outboundSource)),
            "scheduledFor": lambda n : setattr(self, 'scheduled_for', n.get_datetime_value()),
            "selectionReason": lambda n : setattr(self, 'selection_reason', n.get_enum_value(SendSmsRequest_selectionReason)),
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
        writer.write_str_value("automationId", self.automation_id)
        writer.write_str_value("campaignId", self.campaign_id)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_bool_value("hasRequiredConsent", self.has_required_consent)
        writer.write_str_value("importBatchId", self.import_batch_id)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_bool_value("isImportedLead", self.is_imported_lead)
        writer.write_str_value("outboundDeliveryRequestId", self.outbound_delivery_request_id)
        writer.write_str_value("outboundIdempotencyKey", self.outbound_idempotency_key)
        writer.write_enum_value("outboundPriority", self.outbound_priority)
        writer.write_str_value("outboundReservationId", self.outbound_reservation_id)
        writer.write_enum_value("outboundSource", self.outbound_source)
        writer.write_datetime_value("scheduledFor", self.scheduled_for)
        writer.write_enum_value("selectionReason", self.selection_reason)
        writer.write_str_value("smsEventId", self.sms_event_id)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("text", self.text)
        writer.write_bool_value("wasManuallyOverridden", self.was_manually_overridden)
        writer.write_additional_data_value(self.additional_data)
    

