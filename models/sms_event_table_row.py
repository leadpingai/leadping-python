from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sms_event_table_row_outbound_source import SmsEventTableRow_outboundSource
    from .sms_event_table_row_status import SmsEventTableRow_status
    from .sms_event_table_row_traffic_type import SmsEventTableRow_trafficType

@dataclass
class SmsEventTableRow(AdditionalDataHolder, Parsable):
    """
    List item schema for Leadping API SMS event table row results shown in searchable tables.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Display name for the actor that performed the action.
    actor_display_name: Optional[str] = None
    # User ID for the actor that performed the action.
    actor_user_id: Optional[str] = None
    # Billing state for this communication, charge, or transaction.
    billing_status: Optional[str] = None
    # UTC timestamp when Leadping blocked this communication.
    blocked_at: Optional[datetime.datetime] = None
    # Business summary connected to this SMS event table row.
    business: Optional[str] = None
    # Business display name shown for this SMS event.
    business_name: Optional[str] = None
    # Reason this delivery, run, or request was canceled.
    cancel_reason: Optional[str] = None
    # UTC timestamp when this delivery or workflow was canceled.
    canceled_at: Optional[datetime.datetime] = None
    # Compliance action applied to this message, lead, or sender.
    compliance_action: Optional[str] = None
    # Conversation ID that links this SMS event table row to the Leadping inbox thread.
    conversation_id: Optional[str] = None
    # UTC timestamp when this SMS event table row was created.
    created_at: Optional[datetime.datetime] = None
    # UTC timestamp when the provider confirmed delivery.
    delivered_at: Optional[datetime.datetime] = None
    # Communication direction for this SMS event table row, such as inbound or outbound.
    direction: Optional[str] = None
    # Machine-readable error code returned while processing this SMS event table row.
    error_code: Optional[str] = None
    # Human-readable error message returned while processing this SMS event table row.
    error_message: Optional[str] = None
    # UTC timestamp when processing failed for this SMS event table row.
    failed_at: Optional[datetime.datetime] = None
    # Sender phone number used for this communication.
    from_phone_number: Optional[str] = None
    # Sender phone number ID used for this outbound SMS or call.
    from_phone_number_id: Optional[str] = None
    # Unique Leadping identifier for this SMS event table row.
    id: Optional[str] = None
    # Indicates whether automation created or triggered this SMS event table row.
    is_automated: Optional[bool] = None
    # Indicates whether this SMS event table row is part of Leadping sender warmup traffic.
    is_warmup: Optional[bool] = None
    # Lead ID associated with this SMS event.
    lead_id: Optional[str] = None
    # Lead display name shown for this SMS event.
    lead_name: Optional[str] = None
    # Phone number ID selected for outbound delivery.
    outbound_phone_number_id: Optional[str] = None
    # Defines the source that requested outbound delivery.
    outbound_source: Optional[SmsEventTableRow_outboundSource] = None
    # Provider message identifier for SMS delivery tracking and reconciliation.
    provider_message_id: Optional[str] = None
    # UTC timestamp when Leadping queued this SMS event table row for processing.
    queued_at: Optional[datetime.datetime] = None
    # UTC timestamp when Leadping received this inbound event or message.
    received_at: Optional[datetime.datetime] = None
    # UTC timestamp when this SMS event is scheduled to send.
    scheduled_for: Optional[datetime.datetime] = None
    # Reason Leadping scheduled this delivery for a later time.
    scheduled_reason: Optional[str] = None
    # Display name for the sender of this message.
    sender_name: Optional[str] = None
    # UTC timestamp when Leadping began sending this message.
    sending_started_at: Optional[datetime.datetime] = None
    # UTC timestamp when Leadping sent this message to the provider.
    sent_at: Optional[datetime.datetime] = None
    # Defines the supported SMS Message Status values.
    status: Optional[SmsEventTableRow_status] = None
    # Human-readable reason explaining the current status of this SMS event table row.
    status_reason: Optional[str] = None
    # Telnyx identifier connected to this phone number, call, or SMS event.
    telnyx_id: Optional[str] = None
    # 10DLC campaign identifier associated with this sender or SMS event.
    ten_dlc_campaign_id: Optional[str] = None
    # Body text for the SMS message or communication represented by this SMS event table row.
    text: Optional[str] = None
    # Recipient phone number used for this communication.
    to_phone_number: Optional[str] = None
    # Defines the supported SMS Traffic Type values.
    traffic_type: Optional[SmsEventTableRow_trafficType] = None
    # UTC timestamp when the provider marked the message undeliverable.
    undeliverable_at: Optional[datetime.datetime] = None
    # User summary connected to this SMS event table row.
    user: Optional[str] = None
    # Display name for the user connected to this SMS event table row.
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmsEventTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsEventTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmsEventTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sms_event_table_row_outbound_source import SmsEventTableRow_outboundSource
        from .sms_event_table_row_status import SmsEventTableRow_status
        from .sms_event_table_row_traffic_type import SmsEventTableRow_trafficType

        from .sms_event_table_row_outbound_source import SmsEventTableRow_outboundSource
        from .sms_event_table_row_status import SmsEventTableRow_status
        from .sms_event_table_row_traffic_type import SmsEventTableRow_trafficType

        fields: dict[str, Callable[[Any], None]] = {
            "actorDisplayName": lambda n : setattr(self, 'actor_display_name', n.get_str_value()),
            "actorUserId": lambda n : setattr(self, 'actor_user_id', n.get_str_value()),
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_str_value()),
            "blockedAt": lambda n : setattr(self, 'blocked_at', n.get_datetime_value()),
            "business": lambda n : setattr(self, 'business', n.get_str_value()),
            "businessName": lambda n : setattr(self, 'business_name', n.get_str_value()),
            "cancelReason": lambda n : setattr(self, 'cancel_reason', n.get_str_value()),
            "canceledAt": lambda n : setattr(self, 'canceled_at', n.get_datetime_value()),
            "complianceAction": lambda n : setattr(self, 'compliance_action', n.get_str_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "deliveredAt": lambda n : setattr(self, 'delivered_at', n.get_datetime_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isAutomated": lambda n : setattr(self, 'is_automated', n.get_bool_value()),
            "isWarmup": lambda n : setattr(self, 'is_warmup', n.get_bool_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "leadName": lambda n : setattr(self, 'lead_name', n.get_str_value()),
            "outboundPhoneNumberId": lambda n : setattr(self, 'outbound_phone_number_id', n.get_str_value()),
            "outboundSource": lambda n : setattr(self, 'outbound_source', n.get_enum_value(SmsEventTableRow_outboundSource)),
            "providerMessageId": lambda n : setattr(self, 'provider_message_id', n.get_str_value()),
            "queuedAt": lambda n : setattr(self, 'queued_at', n.get_datetime_value()),
            "receivedAt": lambda n : setattr(self, 'received_at', n.get_datetime_value()),
            "scheduledFor": lambda n : setattr(self, 'scheduled_for', n.get_datetime_value()),
            "scheduledReason": lambda n : setattr(self, 'scheduled_reason', n.get_str_value()),
            "senderName": lambda n : setattr(self, 'sender_name', n.get_str_value()),
            "sendingStartedAt": lambda n : setattr(self, 'sending_started_at', n.get_datetime_value()),
            "sentAt": lambda n : setattr(self, 'sent_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SmsEventTableRow_status)),
            "statusReason": lambda n : setattr(self, 'status_reason', n.get_str_value()),
            "telnyxId": lambda n : setattr(self, 'telnyx_id', n.get_str_value()),
            "tenDlcCampaignId": lambda n : setattr(self, 'ten_dlc_campaign_id', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "toPhoneNumber": lambda n : setattr(self, 'to_phone_number', n.get_str_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(SmsEventTableRow_trafficType)),
            "undeliverableAt": lambda n : setattr(self, 'undeliverable_at', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        writer.write_str_value("actorDisplayName", self.actor_display_name)
        writer.write_str_value("actorUserId", self.actor_user_id)
        writer.write_str_value("billingStatus", self.billing_status)
        writer.write_datetime_value("blockedAt", self.blocked_at)
        writer.write_str_value("business", self.business)
        writer.write_str_value("businessName", self.business_name)
        writer.write_str_value("cancelReason", self.cancel_reason)
        writer.write_datetime_value("canceledAt", self.canceled_at)
        writer.write_str_value("complianceAction", self.compliance_action)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_datetime_value("deliveredAt", self.delivered_at)
        writer.write_str_value("direction", self.direction)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isAutomated", self.is_automated)
        writer.write_bool_value("isWarmup", self.is_warmup)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("leadName", self.lead_name)
        writer.write_str_value("outboundPhoneNumberId", self.outbound_phone_number_id)
        writer.write_enum_value("outboundSource", self.outbound_source)
        writer.write_str_value("providerMessageId", self.provider_message_id)
        writer.write_datetime_value("queuedAt", self.queued_at)
        writer.write_datetime_value("receivedAt", self.received_at)
        writer.write_datetime_value("scheduledFor", self.scheduled_for)
        writer.write_str_value("scheduledReason", self.scheduled_reason)
        writer.write_str_value("senderName", self.sender_name)
        writer.write_datetime_value("sendingStartedAt", self.sending_started_at)
        writer.write_datetime_value("sentAt", self.sent_at)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusReason", self.status_reason)
        writer.write_str_value("telnyxId", self.telnyx_id)
        writer.write_str_value("tenDlcCampaignId", self.ten_dlc_campaign_id)
        writer.write_str_value("text", self.text)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_datetime_value("undeliverableAt", self.undeliverable_at)
        writer.write_str_value("user", self.user)
        writer.write_str_value("userName", self.user_name)
        writer.write_additional_data_value(self.additional_data)
    

