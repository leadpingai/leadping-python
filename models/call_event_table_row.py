from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .call_event_table_row_metadata import CallEventTableRow_metadata
    from .call_event_table_row_status import CallEventTableRow_status

@dataclass
class CallEventTableRow(AdditionalDataHolder, Parsable):
    """
    API DTO containing call event data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time for the answered at value on this call event.
    answered_at: Optional[datetime.datetime] = None
    # The billing phone number ID associated with this call event.
    billing_phone_number_id: Optional[str] = None
    # The current billing status for this call event.
    billing_status: Optional[str] = None
    # The business value for this call event.
    business: Optional[str] = None
    # The business ID associated with this call event.
    business_id: Optional[str] = None
    # The caller ID associated with this call event.
    caller_id: Optional[str] = None
    # The conversation ID associated with this call event.
    conversation_id: Optional[str] = None
    # The date and time for the created at value on this call event.
    created_at: Optional[datetime.datetime] = None
    # The direction value for this call event.
    direction: Optional[str] = None
    # The date and time for the ended at value on this call event.
    ended_at: Optional[datetime.datetime] = None
    # The phone number associated with this call event.
    from_phone_number: Optional[str] = None
    # The from phone number ID associated with this call event.
    from_phone_number_id: Optional[str] = None
    # The unique ID for this call event.
    id: Optional[str] = None
    # The lead ID associated with this call event.
    lead_id: Optional[str] = None
    # The metadata key-value data carried with this call event; values must be safe to expose in API responses.
    metadata: Optional[CallEventTableRow_metadata] = None
    # The current provider status for this call event.
    provider_status: Optional[str] = None
    # The URL associated with this call event.
    recording_url: Optional[str] = None
    # Defines the supported Phone Call Status values.
    status: Optional[CallEventTableRow_status] = None
    # The human-readable status reason explaining this call event.
    status_reason: Optional[str] = None
    # The Telnyx ID associated with this call event.
    telnyx_id: Optional[str] = None
    # The phone number associated with this call event.
    to_phone_number: Optional[str] = None
    # The user value for this call event.
    user: Optional[str] = None
    # The user ID associated with this call event.
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
        from .call_event_table_row_metadata import CallEventTableRow_metadata
        from .call_event_table_row_status import CallEventTableRow_status

        from .call_event_table_row_metadata import CallEventTableRow_metadata
        from .call_event_table_row_status import CallEventTableRow_status

        fields: dict[str, Callable[[Any], None]] = {
            "answeredAt": lambda n : setattr(self, 'answered_at', n.get_datetime_value()),
            "billingPhoneNumberId": lambda n : setattr(self, 'billing_phone_number_id', n.get_str_value()),
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
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(CallEventTableRow_metadata)),
            "providerStatus": lambda n : setattr(self, 'provider_status', n.get_str_value()),
            "recordingUrl": lambda n : setattr(self, 'recording_url', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CallEventTableRow_status)),
            "statusReason": lambda n : setattr(self, 'status_reason', n.get_str_value()),
            "telnyxId": lambda n : setattr(self, 'telnyx_id', n.get_str_value()),
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
        writer.write_str_value("billingPhoneNumberId", self.billing_phone_number_id)
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
        writer.write_object_value("metadata", self.metadata)
        writer.write_str_value("providerStatus", self.provider_status)
        writer.write_str_value("recordingUrl", self.recording_url)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusReason", self.status_reason)
        writer.write_str_value("telnyxId", self.telnyx_id)
        writer.write_str_value("toPhoneNumber", self.to_phone_number)
        writer.write_str_value("user", self.user)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

