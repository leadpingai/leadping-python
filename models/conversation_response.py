from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation_response_current_disposition import ConversationResponse_currentDisposition
    from .conversation_response_phone_number import ConversationResponse_phoneNumber
    from .conversation_response_status import ConversationResponse_status

@dataclass
class ConversationResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API conversation response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Phone number ID currently active for outbound delivery.
    active_outbound_phone_number_id: Optional[str] = None
    # Defines why a lead was removed from the active working pipeline.
    archive_reason: Optional[int] = None
    # UTC timestamp when this record was archived.
    archived_at: Optional[datetime.datetime] = None
    # Current disposition summary that describes the lead outcome.
    current_disposition: Optional[ConversationResponse_currentDisposition] = None
    # First name of the lead, user, or contact represented by this conversation response.
    first_name: Optional[str] = None
    # Unique Leadping identifier for this conversation response.
    id: Optional[str] = None
    # Indicates whether the Leadping conversation has been archived.
    is_archived: Optional[bool] = None
    # Indicates whether the current user has unread activity in the conversation.
    is_unread: Optional[bool] = None
    # UTC timestamp when the most recent conversation event occurred.
    last_event_at: Optional[datetime.datetime] = None
    # Last name of the lead, user, or contact represented by this conversation response.
    last_name: Optional[str] = None
    # Most recent message preview shown for the conversation.
    last_snippet: Optional[str] = None
    # Lead ID associated with this inbox conversation.
    lead_id: Optional[str] = None
    # Lead's phone number used for conversation matching and outreach.
    lead_phone_number: Optional[str] = None
    # Recommended next step to move this conversation response forward.
    next_step: Optional[str] = None
    # Phone number ID manually chosen to override automatic outbound selection.
    outbound_phone_number_override_id: Optional[str] = None
    # Phone number used by this conversation response for calls, SMS, lookup, or routing.
    phone_number: Optional[ConversationResponse_phoneNumber] = None
    # Defines the customer-facing operational status for an inbox conversation.
    status: Optional[ConversationResponse_status] = None
    # Human-readable reason explaining the current status of this conversation response.
    status_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConversationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConversationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConversationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conversation_response_current_disposition import ConversationResponse_currentDisposition
        from .conversation_response_phone_number import ConversationResponse_phoneNumber
        from .conversation_response_status import ConversationResponse_status

        from .conversation_response_current_disposition import ConversationResponse_currentDisposition
        from .conversation_response_phone_number import ConversationResponse_phoneNumber
        from .conversation_response_status import ConversationResponse_status

        fields: dict[str, Callable[[Any], None]] = {
            "activeOutboundPhoneNumberId": lambda n : setattr(self, 'active_outbound_phone_number_id', n.get_str_value()),
            "archiveReason": lambda n : setattr(self, 'archive_reason', n.get_int_value()),
            "archivedAt": lambda n : setattr(self, 'archived_at', n.get_datetime_value()),
            "currentDisposition": lambda n : setattr(self, 'current_disposition', n.get_object_value(ConversationResponse_currentDisposition)),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isArchived": lambda n : setattr(self, 'is_archived', n.get_bool_value()),
            "isUnread": lambda n : setattr(self, 'is_unread', n.get_bool_value()),
            "lastEventAt": lambda n : setattr(self, 'last_event_at', n.get_datetime_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "lastSnippet": lambda n : setattr(self, 'last_snippet', n.get_str_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "leadPhoneNumber": lambda n : setattr(self, 'lead_phone_number', n.get_str_value()),
            "nextStep": lambda n : setattr(self, 'next_step', n.get_str_value()),
            "outboundPhoneNumberOverrideId": lambda n : setattr(self, 'outbound_phone_number_override_id', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_object_value(ConversationResponse_phoneNumber)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ConversationResponse_status)),
            "statusReason": lambda n : setattr(self, 'status_reason', n.get_str_value()),
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
        writer.write_str_value("activeOutboundPhoneNumberId", self.active_outbound_phone_number_id)
        writer.write_int_value("archiveReason", self.archive_reason)
        writer.write_datetime_value("archivedAt", self.archived_at)
        writer.write_object_value("currentDisposition", self.current_disposition)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isArchived", self.is_archived)
        writer.write_bool_value("isUnread", self.is_unread)
        writer.write_datetime_value("lastEventAt", self.last_event_at)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("lastSnippet", self.last_snippet)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("leadPhoneNumber", self.lead_phone_number)
        writer.write_str_value("nextStep", self.next_step)
        writer.write_str_value("outboundPhoneNumberOverrideId", self.outbound_phone_number_override_id)
        writer.write_object_value("phoneNumber", self.phone_number)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusReason", self.status_reason)
        writer.write_additional_data_value(self.additional_data)
    

