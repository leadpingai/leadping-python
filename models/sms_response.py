from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sms_response_selection_reason import SmsResponse_selectionReason
    from .sms_response_status import SmsResponse_status
    from .sms_response_traffic_type import SmsResponse_trafficType

@dataclass
class SmsResponse(AdditionalDataHolder, Parsable):
    """
    API response containing SMS data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The current billing status for this SMS.
    billing_status: Optional[str] = None
    # The date and time for the blocked at value on this SMS.
    blocked_at: Optional[datetime.datetime] = None
    # The campaign ID associated with this SMS.
    campaign_id: Optional[str] = None
    # The human-readable cancel reason explaining this SMS.
    cancel_reason: Optional[str] = None
    # The date and time for the canceled at value on this SMS.
    canceled_at: Optional[datetime.datetime] = None
    # The compliance action value for this SMS.
    compliance_action: Optional[str] = None
    # The conversation ID associated with this SMS.
    conversation_id: Optional[str] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # The date and time for the delivered at value on this SMS.
    delivered_at: Optional[datetime.datetime] = None
    # The error code value for this SMS.
    error_code: Optional[str] = None
    # The error message value for this SMS.
    error_message: Optional[str] = None
    # The date and time for the failed at value on this SMS.
    failed_at: Optional[datetime.datetime] = None
    # The phone number associated with this SMS.
    from_phone_number: Optional[str] = None
    # The from phone number ID associated with this SMS.
    from_phone_number_id: Optional[str] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # Whether this SMS is warmup.
    is_warmup: Optional[bool] = None
    # The lead ID associated with this SMS.
    lead_id: Optional[str] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The date and time for the next retry at value on this SMS.
    next_retry_at: Optional[datetime.datetime] = None
    # The outbound phone number ID associated with this SMS.
    outbound_phone_number_id: Optional[str] = None
    # The provider message ID associated with this SMS.
    provider_message_id: Optional[str] = None
    # The date and time for the queued at value on this SMS.
    queued_at: Optional[datetime.datetime] = None
    # The date and time for the received at value on this SMS.
    received_at: Optional[datetime.datetime] = None
    # The retry count for this SMS.
    retry_count: Optional[int] = None
    # The date and time for the scheduled for value on this SMS.
    scheduled_for: Optional[datetime.datetime] = None
    # The human-readable scheduled reason explaining this SMS.
    scheduled_reason: Optional[str] = None
    # Defines the supported Outgoing Number Selection Reason values.
    selection_reason: Optional[SmsResponse_selectionReason] = None
    # The date and time for the sending started at value on this SMS.
    sending_started_at: Optional[datetime.datetime] = None
    # The date and time for the sent at value on this SMS.
    sent_at: Optional[datetime.datetime] = None
    # The source ID associated with this SMS.
    source_id: Optional[str] = None
    # Defines the supported SMS Message Status values.
    status: Optional[SmsResponse_status] = None
    # The human-readable status reason explaining this SMS.
    status_reason: Optional[str] = None
    # The Telnyx ID associated with this SMS.
    telnyx_id: Optional[str] = None
    # The 10DLC campaign ID associated with this SMS.
    ten_dlc_campaign_id: Optional[str] = None
    # The text value for this SMS.
    text: Optional[str] = None
    # Defines the supported SMS Traffic Type values.
    traffic_type: Optional[SmsResponse_trafficType] = None
    # The date and time for the undeliverable at value on this SMS.
    undeliverable_at: Optional[datetime.datetime] = None
    # Whether this SMS was manually overridden.
    was_manually_overridden: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sms_response_selection_reason import SmsResponse_selectionReason
        from .sms_response_status import SmsResponse_status
        from .sms_response_traffic_type import SmsResponse_trafficType

        from .sms_response_selection_reason import SmsResponse_selectionReason
        from .sms_response_status import SmsResponse_status
        from .sms_response_traffic_type import SmsResponse_trafficType

        fields: dict[str, Callable[[Any], None]] = {
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_str_value()),
            "blockedAt": lambda n : setattr(self, 'blocked_at', n.get_datetime_value()),
            "campaignId": lambda n : setattr(self, 'campaign_id', n.get_str_value()),
            "cancelReason": lambda n : setattr(self, 'cancel_reason', n.get_str_value()),
            "canceledAt": lambda n : setattr(self, 'canceled_at', n.get_datetime_value()),
            "complianceAction": lambda n : setattr(self, 'compliance_action', n.get_str_value()),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "deliveredAt": lambda n : setattr(self, 'delivered_at', n.get_datetime_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "errorMessage": lambda n : setattr(self, 'error_message', n.get_str_value()),
            "failedAt": lambda n : setattr(self, 'failed_at', n.get_datetime_value()),
            "fromPhoneNumber": lambda n : setattr(self, 'from_phone_number', n.get_str_value()),
            "fromPhoneNumberId": lambda n : setattr(self, 'from_phone_number_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isWarmup": lambda n : setattr(self, 'is_warmup', n.get_bool_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "nextRetryAt": lambda n : setattr(self, 'next_retry_at', n.get_datetime_value()),
            "outboundPhoneNumberId": lambda n : setattr(self, 'outbound_phone_number_id', n.get_str_value()),
            "providerMessageId": lambda n : setattr(self, 'provider_message_id', n.get_str_value()),
            "queuedAt": lambda n : setattr(self, 'queued_at', n.get_datetime_value()),
            "receivedAt": lambda n : setattr(self, 'received_at', n.get_datetime_value()),
            "retryCount": lambda n : setattr(self, 'retry_count', n.get_int_value()),
            "scheduledFor": lambda n : setattr(self, 'scheduled_for', n.get_datetime_value()),
            "scheduledReason": lambda n : setattr(self, 'scheduled_reason', n.get_str_value()),
            "selectionReason": lambda n : setattr(self, 'selection_reason', n.get_enum_value(SmsResponse_selectionReason)),
            "sendingStartedAt": lambda n : setattr(self, 'sending_started_at', n.get_datetime_value()),
            "sentAt": lambda n : setattr(self, 'sent_at', n.get_datetime_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SmsResponse_status)),
            "statusReason": lambda n : setattr(self, 'status_reason', n.get_str_value()),
            "telnyxId": lambda n : setattr(self, 'telnyx_id', n.get_str_value()),
            "tenDlcCampaignId": lambda n : setattr(self, 'ten_dlc_campaign_id', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
            "trafficType": lambda n : setattr(self, 'traffic_type', n.get_enum_value(SmsResponse_trafficType)),
            "undeliverableAt": lambda n : setattr(self, 'undeliverable_at', n.get_datetime_value()),
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
        writer.write_str_value("billingStatus", self.billing_status)
        writer.write_datetime_value("blockedAt", self.blocked_at)
        writer.write_str_value("campaignId", self.campaign_id)
        writer.write_str_value("cancelReason", self.cancel_reason)
        writer.write_datetime_value("canceledAt", self.canceled_at)
        writer.write_str_value("complianceAction", self.compliance_action)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_datetime_value("deliveredAt", self.delivered_at)
        writer.write_str_value("errorCode", self.error_code)
        writer.write_str_value("errorMessage", self.error_message)
        writer.write_datetime_value("failedAt", self.failed_at)
        writer.write_str_value("fromPhoneNumber", self.from_phone_number)
        writer.write_str_value("fromPhoneNumberId", self.from_phone_number_id)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isWarmup", self.is_warmup)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_datetime_value("nextRetryAt", self.next_retry_at)
        writer.write_str_value("outboundPhoneNumberId", self.outbound_phone_number_id)
        writer.write_str_value("providerMessageId", self.provider_message_id)
        writer.write_datetime_value("queuedAt", self.queued_at)
        writer.write_datetime_value("receivedAt", self.received_at)
        writer.write_int_value("retryCount", self.retry_count)
        writer.write_datetime_value("scheduledFor", self.scheduled_for)
        writer.write_str_value("scheduledReason", self.scheduled_reason)
        writer.write_enum_value("selectionReason", self.selection_reason)
        writer.write_datetime_value("sendingStartedAt", self.sending_started_at)
        writer.write_datetime_value("sentAt", self.sent_at)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusReason", self.status_reason)
        writer.write_str_value("telnyxId", self.telnyx_id)
        writer.write_str_value("tenDlcCampaignId", self.ten_dlc_campaign_id)
        writer.write_str_value("text", self.text)
        writer.write_enum_value("trafficType", self.traffic_type)
        writer.write_datetime_value("undeliverableAt", self.undeliverable_at)
        writer.write_bool_value("wasManuallyOverridden", self.was_manually_overridden)
        writer.write_additional_data_value(self.additional_data)
    

