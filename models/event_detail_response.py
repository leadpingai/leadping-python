from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_detail_response_status import EventDetailResponse_status
    from .event_detail_response_timeline_type import EventDetailResponse_timelineType
    from .event_detail_response_user import EventDetailResponse_user

@dataclass
class EventDetailResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API event detail response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp when Leadping blocked this communication.
    blocked_at: Optional[datetime.datetime] = None
    # UTC timestamp when this delivery or workflow was canceled.
    canceled_at: Optional[datetime.datetime] = None
    # Conversation ID that links this event detail response to the Leadping inbox thread.
    conversation_id: Optional[str] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # UTC timestamp when the provider confirmed delivery.
    delivered_at: Optional[datetime.datetime] = None
    # Human-readable description that explains this event detail response to API users.
    description: Optional[str] = None
    # Communication direction for this event detail response, such as inbound or outbound.
    direction: Optional[str] = None
    # High-level category used to group this Leadping event.
    event_category: Optional[str] = None
    # Event type used to classify this timeline, SMS, call, or automation event.
    event_type: Optional[str] = None
    # UTC timestamp when processing failed for this event detail response.
    failed_at: Optional[datetime.datetime] = None
    # Sender phone number used for this communication.
    from_phone_number: Optional[str] = None
    # Sender phone number ID used for this outbound SMS or call.
    from_phone_number_id: Optional[str] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # Lead ID associated with this event detail record.
    lead_id: Optional[str] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # Phone number ID selected for outbound delivery.
    outbound_phone_number_id: Optional[str] = None
    # Provider message identifier for SMS delivery tracking and reconciliation.
    provider_message_id: Optional[str] = None
    # UTC timestamp when Leadping queued this event detail response for processing.
    queued_at: Optional[datetime.datetime] = None
    # UTC timestamp when Leadping received this inbound event or message.
    received_at: Optional[datetime.datetime] = None
    # UTC timestamp when the related delivery or workflow action is scheduled to run.
    scheduled_for: Optional[datetime.datetime] = None
    # Secondary event type used for additional event classification.
    secondary_event_type: Optional[str] = None
    # UTC timestamp when Leadping began sending this message.
    sending_started_at: Optional[datetime.datetime] = None
    # UTC timestamp when Leadping sent this message to the provider.
    sent_at: Optional[datetime.datetime] = None
    # Defines the supported Event status values.
    status: Optional[EventDetailResponse_status] = None
    # Human-readable reason explaining the current status of this event detail response.
    status_reason: Optional[str] = None
    # Short human-readable summary of this event detail response for lists, timelines, and notifications.
    summary: Optional[str] = None
    # Timeline category used to group events for display and filtering.
    timeline_category: Optional[str] = None
    # Defines the supported Event timeline type values.
    timeline_type: Optional[EventDetailResponse_timelineType] = None
    # Recipient phone number used for this communication.
    to_phone_number: Optional[str] = None
    # UTC timestamp when the provider marked the message undeliverable.
    undeliverable_at: Optional[datetime.datetime] = None
    # User summary connected to this event detail response.
    user: Optional[EventDetailResponse_user] = None
    # User ID associated with the activity that created this event.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EventDetailResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EventDetailResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EventDetailResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .event_detail_response_status import EventDetailResponse_status
        from .event_detail_response_timeline_type import EventDetailResponse_timelineType
        from .event_detail_response_user import EventDetailResponse_user

        from .event_detail_response_status import EventDetailResponse_status
        from .event_detail_response_timeline_type import EventDetailResponse_timelineType
        from .event_detail_response_user import EventDetailResponse_user

        fields: dict[str, Callable[[Any], None]] = {
            "blockedAt": lambda n : setattr(self, 'blocked_at', n.get_datetime_value()),
            "canceledAt": lambda n : setattr(self, 'canceled_at', n.get_datetime_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "deliveredAt": lambda n : setattr(self, 'delivered_at', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "eventCategory": lambda n : setattr(self, 'event_category', n.get_str_value()),
            "eventType": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "outboundPhoneNumberId": lambda n : setattr(self, 'outbound_phone_number_id', n.get_str_value()),
            "providerMessageId": lambda n : setattr(self, 'provider_message_id', n.get_str_value()),
            "queuedAt": lambda n : setattr(self, 'queued_at', n.get_datetime_value()),
            "receivedAt": lambda n : setattr(self, 'received_at', n.get_datetime_value()),
            "scheduledFor": lambda n : setattr(self, 'scheduled_for', n.get_datetime_value()),
            "secondaryEventType": lambda n : setattr(self, 'secondary_event_type', n.get_str_value()),
            "sendingStartedAt": lambda n : setattr(self, 'sending_started_at', n.get_datetime_value()),
            "sentAt": lambda n : setattr(self, 'sent_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(EventDetailResponse_status)),
            "statusReason": lambda n : setattr(self, 'status_reason', n.get_str_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
            "timelineCategory": lambda n : setattr(self, 'timeline_category', n.get_str_value()),
            "timelineType": lambda n : setattr(self, 'timeline_type', n.get_enum_value(EventDetailResponse_timelineType)),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
            "undeliverableAt": lambda n : setattr(self, 'undeliverable_at', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(EventDetailResponse_user)),
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
        writer.write_datetime_value("blockedAt", self.blocked_at)
        writer.write_datetime_value("canceledAt", self.canceled_at)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_datetime_value("deliveredAt", self.delivered_at)
        writer.write_str_value("description", self.description)
        writer.write_str_value("direction", self.direction)
        writer.write_str_value("eventCategory", self.event_category)
        writer.write_str_value("eventType", self.event_type)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("outboundPhoneNumberId", self.outbound_phone_number_id)
        writer.write_str_value("providerMessageId", self.provider_message_id)
        writer.write_datetime_value("queuedAt", self.queued_at)
        writer.write_datetime_value("receivedAt", self.received_at)
        writer.write_datetime_value("scheduledFor", self.scheduled_for)
        writer.write_str_value("secondaryEventType", self.secondary_event_type)
        writer.write_datetime_value("sendingStartedAt", self.sending_started_at)
        writer.write_datetime_value("sentAt", self.sent_at)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusReason", self.status_reason)
        writer.write_str_value("summary", self.summary)
        writer.write_str_value("timelineCategory", self.timeline_category)
        writer.write_enum_value("timelineType", self.timeline_type)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_datetime_value("undeliverableAt", self.undeliverable_at)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

