from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_event_table_row_status import CallEventTableRow_status
    from .communication_console_entry import CommunicationConsoleEntry

@dataclass
class CallEventTableRow(AdditionalDataHolder, Parsable):
    """
    Summarizes call event data in paginated and searchable results.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp when the call was answered.
    answered_at: Optional[datetime.datetime] = None
    # Monetary amount billed for this Leadping communication or transaction.
    billable_amount: Optional[float] = None
    # Billable call duration in seconds.
    billable_seconds: Optional[int] = None
    # Billing state for this communication, charge, or transaction.
    billing_status: Optional[str] = None
    # Caller ID phone number presented during the outbound call.
    caller_id: Optional[str] = None
    # Ordered diagnostic entries recorded while Leadping processed this call.
    console_entries: Optional[list[CommunicationConsoleEntry]] = None
    # Conversation ID that links this call event table row to the Leadping inbox thread.
    conversation_id: Optional[str] = None
    # UTC timestamp when this call event table row was created.
    created_at: Optional[datetime.datetime] = None
    # Communication direction for this call event table row, such as inbound or outbound.
    direction: Optional[str] = None
    # Call duration or processing duration represented by this call event table row.
    duration: Optional[int] = None
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
    # Display name for the lead associated with this call event.
    lead_name: Optional[str] = None
    # Organization summary connected to this call event table row.
    organization: Optional[str] = None
    # Organization ID associated with this call event.
    organization_id: Optional[str] = None
    # Display name for the organization associated with this call event.
    organization_name: Optional[str] = None
    # Describes the durable business outcome of a Leadping phone call after provider status normalization.
    status: Optional[CallEventTableRow_status] = None
    # Human-readable reason explaining the current status of this call event table row.
    status_reason: Optional[str] = None
    # Recipient phone number used for this communication.
    to_phone_number: Optional[str] = None
    # User summary connected to this call event table row.
    user: Optional[str] = None
    # Email address for the person or agent who initiated this call event.
    user_email: Optional[str] = None
    # User ID associated with the person or agent who initiated this call event.
    user_id: Optional[str] = None
    # Display name for the person or agent who initiated this call event.
    user_name: Optional[str] = None
    # URL for voicemail audio, when the call resulted in a voicemail.
    voicemail_url: Optional[str] = None
    
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
        from .communication_console_entry import CommunicationConsoleEntry

        from .call_event_table_row_status import CallEventTableRow_status
        from .communication_console_entry import CommunicationConsoleEntry

        fields: dict[str, Callable[[Any], None]] = {
            "answeredAt": lambda n : setattr(self, 'answered_at', n.get_datetime_value()),
            "billableAmount": lambda n : setattr(self, 'billable_amount', n.get_float_value()),
            "billableSeconds": lambda n : setattr(self, 'billable_seconds', n.get_int_value()),
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_str_value()),
            "callerId": lambda n : setattr(self, 'caller_id', n.get_str_value()),
            "consoleEntries": lambda n : setattr(self, 'console_entries', n.get_collection_of_object_values(CommunicationConsoleEntry)),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "endedAt": lambda n : setattr(self, 'ended_at', n.get_datetime_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "leadName": lambda n : setattr(self, 'lead_name', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "organizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CallEventTableRow_status)),
            "statusReason": lambda n : setattr(self, 'status_reason', n.get_str_value()),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
            "userEmail": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "voicemailUrl": lambda n : setattr(self, 'voicemail_url', n.get_str_value()),
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
        writer.write_float_value("billableAmount", self.billable_amount)
        writer.write_int_value("billableSeconds", self.billable_seconds)
        writer.write_str_value("billingStatus", self.billing_status)
        writer.write_str_value("callerId", self.caller_id)
        writer.write_collection_of_object_values("consoleEntries", self.console_entries)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("direction", self.direction)
        writer.write_int_value("duration", self.duration)
        writer.write_datetime_value("endedAt", self.ended_at)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("leadName", self.lead_name)
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusReason", self.status_reason)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_str_value("user", self.user)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("voicemailUrl", self.voicemail_url)
        writer.write_additional_data_value(self.additional_data)
    

