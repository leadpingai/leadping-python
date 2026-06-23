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
    API response containing conversation data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The active outbound phone number ID associated with this conversation.
    active_outbound_phone_number_id: Optional[str] = None
    # Defines why a lead was removed from the active working pipeline.
    archive_reason: Optional[int] = None
    # The archivedAt property
    archived_at: Optional[datetime.datetime] = None
    # The current lifecycle disposition for the conversation's lead.
    current_disposition: Optional[ConversationResponse_currentDisposition] = None
    # The first name value for this conversation.
    first_name: Optional[str] = None
    # The unique ID for this conversation.
    id: Optional[str] = None
    # The isArchived property
    is_archived: Optional[bool] = None
    # Whether this conversation is unread.
    is_unread: Optional[bool] = None
    # The date and time for the last event at value on this conversation.
    last_event_at: Optional[datetime.datetime] = None
    # The date and time for the last name value on this conversation.
    last_name: Optional[str] = None
    # The date and time for the last snippet value on this conversation.
    last_snippet: Optional[str] = None
    # The lead ID associated with this conversation.
    lead_id: Optional[str] = None
    # The lead's primary contact phone number for this conversation.
    lead_phone_number: Optional[str] = None
    # The recommended next action for the inbox user.
    next_step: Optional[str] = None
    # The outbound phone number override ID associated with this conversation.
    outbound_phone_number_override_id: Optional[str] = None
    # The Leadping sender phone number associated with this conversation.
    phone_number: Optional[ConversationResponse_phoneNumber] = None
    # Defines the customer-facing operational status for an inbox conversation.
    status: Optional[ConversationResponse_status] = None
    # The human-readable reason explaining the current conversation status.
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
    

