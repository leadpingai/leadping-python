from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_call_response_selection_reason import PhoneCallResponse_selectionReason
    from .phone_call_status import PhoneCallStatus

@dataclass
class PhoneCallResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API phone call returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp when the call was answered.
    answered_at: Optional[datetime.datetime] = None
    # Billing state for this communication, charge, or transaction.
    billing_status: Optional[str] = None
    # Caller ID phone number presented during the outbound call.
    caller_id: Optional[str] = None
    # Messaging campaign identifier associated with this phone call.
    campaign_id: Optional[str] = None
    # Conversation ID that links this phone call to the Leadping inbox thread.
    conversation_id: Optional[str] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # Communication direction for this phone call, such as inbound or outbound.
    direction: Optional[str] = None
    # UTC timestamp when the call ended.
    ended_at: Optional[datetime.datetime] = None
    # Sender phone number used for this communication.
    from_phone_number: Optional[str] = None
    # Sender phone number ID used for this outbound SMS or call.
    from_phone_number_id: Optional[str] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # Lead ID associated with the call conversation or outreach attempt.
    lead_id: Optional[str] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # Phone number used by this phone call for calls, SMS, lookup, or routing.
    phone_number: Optional[str] = None
    # UTC timestamp when Leadping queued this phone call for processing.
    queued_at: Optional[datetime.datetime] = None
    # URL for the call recording, when the provider makes one available.
    recording_url: Optional[str] = None
    # UTC timestamp when the call started ringing.
    ringing_at: Optional[datetime.datetime] = None
    # Defines the supported Outgoing Number Selection Reason values.
    selection_reason: Optional[PhoneCallResponse_selectionReason] = None
    # Lead source ID used for attribution and routing on this call.
    source_id: Optional[str] = None
    # Current lifecycle status for this phone call in the Leadping API.
    status: Optional[PhoneCallStatus] = None
    # Human-readable reason explaining the current status of this phone call.
    status_reason: Optional[str] = None
    # Recipient phone number used for this communication.
    to_phone_number: Optional[str] = None
    # Indicates whether a user manually overrode Leadping's automatic number selection for this phone call.
    was_manually_overridden: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneCallResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneCallResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneCallResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_call_response_selection_reason import PhoneCallResponse_selectionReason
        from .phone_call_status import PhoneCallStatus

        from .phone_call_response_selection_reason import PhoneCallResponse_selectionReason
        from .phone_call_status import PhoneCallStatus

        fields: dict[str, Callable[[Any], None]] = {
            "answeredAt": lambda n : setattr(self, 'answered_at', n.get_datetime_value()),
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_str_value()),
            "callerId": lambda n : setattr(self, 'caller_id', n.get_str_value()),
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "endedAt": lambda n : setattr(self, 'ended_at', n.get_datetime_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "queuedAt": lambda n : setattr(self, 'queued_at', n.get_datetime_value()),
            "recordingUrl": lambda n : setattr(self, 'recording_url', n.get_str_value()),
            "ringingAt": lambda n : setattr(self, 'ringing_at', n.get_datetime_value()),
            "selectionReason": lambda n : setattr(self, 'selection_reason', n.get_enum_value(PhoneCallResponse_selectionReason)),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(PhoneCallStatus)),
            "statusReason": lambda n : setattr(self, 'status_reason', n.get_str_value()),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
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
        writer.write_datetime_value("answeredAt", self.answered_at)
        writer.write_str_value("billingStatus", self.billing_status)
        writer.write_str_value("callerId", self.caller_id)
        writer.write_str_value("campaignId", self.campaign_id)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("direction", self.direction)
        writer.write_datetime_value("endedAt", self.ended_at)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_datetime_value("queuedAt", self.queued_at)
        writer.write_str_value("recordingUrl", self.recording_url)
        writer.write_datetime_value("ringingAt", self.ringing_at)
        writer.write_enum_value("selectionReason", self.selection_reason)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusReason", self.status_reason)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_bool_value("wasManuallyOverridden", self.was_manually_overridden)
        writer.write_additional_data_value(self.additional_data)
    

