from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .initiate_call_request_outbound_priority import InitiateCallRequest_outboundPriority
    from .initiate_call_request_outbound_source import InitiateCallRequest_outboundSource
    from .initiate_call_request_selection_reason import InitiateCallRequest_selectionReason

@dataclass
class InitiateCallRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API phone call initiation request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Automation ID connected to this workflow, run, or event.
    automation_id: Optional[str] = None
    # Messaging campaign identifier associated with this phone call initiation request.
    campaign_id: Optional[str] = None
    # Conversation ID that links this phone call initiation request to the Leadping inbox thread.
    conversation_id: Optional[str] = None
    # Sender phone number ID used for this outbound SMS or call.
    from_phone_number_id: Optional[str] = None
    # Bulk import batch ID that created or updated this lead.
    import_batch_id: Optional[str] = None
    # Indicates whether automation created or triggered this phone call initiation request.
    is_automated: Optional[bool] = None
    # Indicates whether this record originated from a bulk import rather than a real-time lead source.
    is_imported_lead: Optional[bool] = None
    # Lead ID associated with the outbound call request.
    lead_id: Optional[str] = None
    # Outbound delivery request ID connected to this decision or attempt.
    outbound_delivery_request_id: Optional[str] = None
    # Idempotency key used to prevent duplicate outbound delivery.
    outbound_idempotency_key: Optional[str] = None
    # Defines priority classes used when pacing outbound delivery.
    outbound_priority: Optional[InitiateCallRequest_outboundPriority] = None
    # Outbound reservation ID used to throttle and track delivery capacity.
    outbound_reservation_id: Optional[str] = None
    # Defines the source that requested outbound delivery.
    outbound_source: Optional[InitiateCallRequest_outboundSource] = None
    # Defines the supported Outgoing Number Selection Reason values.
    selection_reason: Optional[InitiateCallRequest_selectionReason] = None
    # Lead source ID used for call attribution and sender selection.
    source_id: Optional[str] = None
    # Indicates whether a user manually overrode Leadping's automatic number selection for this phone call initiation request.
    was_manually_overridden: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InitiateCallRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InitiateCallRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InitiateCallRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .initiate_call_request_outbound_priority import InitiateCallRequest_outboundPriority
        from .initiate_call_request_outbound_source import InitiateCallRequest_outboundSource
        from .initiate_call_request_selection_reason import InitiateCallRequest_selectionReason

        from .initiate_call_request_outbound_priority import InitiateCallRequest_outboundPriority
        from .initiate_call_request_outbound_source import InitiateCallRequest_outboundSource
        from .initiate_call_request_selection_reason import InitiateCallRequest_selectionReason

        fields: dict[str, Callable[[Any], None]] = {
            "automationId": lambda n : setattr(self, 'automation_id', n.get_str_value()),
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "importBatchId": lambda n : setattr(self, 'import_batch_id', n.get_str_value()),
            "isAutomated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "isImportedLead": lambda n : setattr(self, 'is_imported_lead', n.get_bool_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "outboundDeliveryRequestId": lambda n : setattr(self, 'outbound_delivery_request_id', n.get_str_value()),
            "outboundIdempotencyKey": lambda n : setattr(self, 'outbound_idempotency_key', n.get_str_value()),
            "outboundPriority": lambda n : setattr(self, 'outbound_priority', n.get_enum_value(InitiateCallRequest_outboundPriority)),
            "outboundReservationId": lambda n : setattr(self, 'outbound_reservation_id', n.get_str_value()),
            "outboundSource": lambda n : setattr(self, 'outbound_source', n.get_enum_value(InitiateCallRequest_outboundSource)),
            "selectionReason": lambda n : setattr(self, 'selection_reason', n.get_enum_value(InitiateCallRequest_selectionReason)),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
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
        writer.write_str_value("importBatchId", self.import_batch_id)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_bool_value("isImportedLead", self.is_imported_lead)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("outboundDeliveryRequestId", self.outbound_delivery_request_id)
        writer.write_str_value("outboundIdempotencyKey", self.outbound_idempotency_key)
        writer.write_enum_value("outboundPriority", self.outbound_priority)
        writer.write_str_value("outboundReservationId", self.outbound_reservation_id)
        writer.write_enum_value("outboundSource", self.outbound_source)
        writer.write_enum_value("selectionReason", self.selection_reason)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_bool_value("wasManuallyOverridden", self.was_manually_overridden)
        writer.write_additional_data_value(self.additional_data)
    

