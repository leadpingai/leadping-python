from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_event_table_row_status import CallEventTableRow_status

@dataclass
class CallEventTableRow(AdditionalDataHolder, Parsable):
    """
    List item schema for Leadping API call event table row results shown in searchable tables.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp when the call was answered.
    answered_at: Optional[datetime.datetime] = None
    # Billing state for this communication, charge, or transaction.
    billing_status: Optional[str] = None
    # Business summary connected to this call event table row.
    business: Optional[str] = None
    # Business ID associated with this call event.
    business_id: Optional[str] = None
    # Caller ID phone number presented during the outbound call.
    caller_id: Optional[str] = None
    # Conversation ID that links this call event table row to the Leadping inbox thread.
    conversation_id: Optional[str] = None
    # UTC timestamp when this call event table row was created.
    created_at: Optional[datetime.datetime] = None
    # Communication direction for this call event table row, such as inbound or outbound.
    direction: Optional[str] = None
    # UTC timestamp when the call ended.
    ended_at: Optional[datetime.datetime] = None
    # Sender phone number used for this communication.
    from_phone_number: Optional[str] = None
    # Sender phone number ID used for this outbound SMS or call.
    from_phone_number_id: Optional[str] = None
    # Unique Leadping identifier for this call event table row.
    id: Optional[str] = None
    # Lead ID associated with this call event.
    lead_id: Optional[str] = None
    # URL for the call recording, when the provider makes one available.
    recording_url: Optional[str] = None
    # Defines the supported Phone Call Status values.
    status: Optional[CallEventTableRow_status] = None
    # Human-readable reason explaining the current status of this call event table row.
    status_reason: Optional[str] = None
    # Recipient phone number used for this communication.
    to_phone_number: Optional[str] = None
    # User summary connected to this call event table row.
    user: Optional[str] = None
    # User ID associated with the person or agent who initiated this call event.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallEventTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallEventTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CallEventTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .call_event_table_row_status import CallEventTableRow_status

        from .call_event_table_row_status import CallEventTableRow_status

        fields: dict[str, Callable[[Any], None]] = {
            "answeredAt": lambda n : setattr(self, 'answered_at', n.get_datetime_value()),
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_str_value()),
            "business": lambda n : setattr(self, 'business', n.get_str_value()),
            "businessId": lambda n : setattr(self, 'business_id', n.get_str_value()),
            "callerId": lambda n : setattr(self, 'caller_id', n.get_str_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "endedAt": lambda n : setattr(self, 'ended_at', n.get_datetime_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "recordingUrl": lambda n : setattr(self, 'recording_url', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CallEventTableRow_status)),
            "statusReason": lambda n : setattr(self, 'status_reason', n.get_str_value()),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("business", self.business)
        writer.write_str_value("businessId", self.business_id)
        writer.write_str_value("callerId", self.caller_id)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("direction", self.direction)
        writer.write_datetime_value("endedAt", self.ended_at)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("recordingUrl", self.recording_url)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusReason", self.status_reason)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_str_value("user", self.user)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

