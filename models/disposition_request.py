from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disposition_request_category import DispositionRequest_category
    from .disposition_request_change_source import DispositionRequest_changeSource

@dataclass
class DispositionRequest(AdditionalDataHolder, Parsable):
    """
    Request model for creating or updating a disposition.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time for the appointment end at value on this disposition.
    appointment_end_at: Optional[datetime.datetime] = None
    # The appointment notes value for this disposition.
    appointment_notes: Optional[str] = None
    # The date and time for the appointment start at value on this disposition.
    appointment_start_at: Optional[datetime.datetime] = None
    # The assigned to user ID associated with this disposition.
    assigned_to_user_id: Optional[str] = None
    # The date and time for the callback at value on this disposition.
    callback_at: Optional[datetime.datetime] = None
    # Controlled disposition categories used for reporting, automation, and analytics.
    category: Optional[DispositionRequest_category] = None
    # Known sources that can change a lead's current disposition.
    change_source: Optional[DispositionRequest_changeSource] = None
    # The automation that changed this disposition, when applicable.
    changed_by_automation_id: Optional[str] = None
    # The current follow up status for this disposition.
    follow_up_status: Optional[str] = None
    # Whether this disposition is missed call follow up.
    is_missed_call_follow_up: Optional[bool] = None
    # The lead ID associated with this disposition.
    lead_id: Optional[str] = None
    # The operator or customer notes recorded for this disposition.
    notes: Optional[str] = None
    # The outcome value for this disposition.
    outcome: Optional[str] = None
    # The reason this disposition was changed.
    reason: Optional[str] = None
    # The related call event ID associated with this disposition.
    related_call_event_id: Optional[str] = None
    # The source ID associated with this disposition.
    source_id: Optional[str] = None
    # The date and time for the task due at value on this disposition.
    task_due_at: Optional[datetime.datetime] = None
    # The date and time for the timestamp value on this disposition.
    timestamp: Optional[datetime.datetime] = None
    # The type classification for this disposition.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispositionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispositionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispositionRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .disposition_request_category import DispositionRequest_category
        from .disposition_request_change_source import DispositionRequest_changeSource

        from .disposition_request_category import DispositionRequest_category
        from .disposition_request_change_source import DispositionRequest_changeSource

        fields: dict[str, Callable[[Any], None]] = {
            "appointmentEndAt": lambda n : setattr(self, 'appointment_end_at', n.get_datetime_value()),
            "appointmentNotes": lambda n : setattr(self, 'appointment_notes', n.get_str_value()),
            "appointmentStartAt": lambda n : setattr(self, 'appointment_start_at', n.get_datetime_value()),
            "assignedToUserId": lambda n : setattr(self, 'assigned_to_user_id', n.get_str_value()),
            "callbackAt": lambda n : setattr(self, 'callback_at', n.get_datetime_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(DispositionRequest_category)),
            "changeSource": lambda n : setattr(self, 'change_source', n.get_enum_value(DispositionRequest_changeSource)),
            "changedByAutomationId": lambda n : setattr(self, 'changed_by_automation_id', n.get_str_value()),
            "followUpStatus": lambda n : setattr(self, 'follow_up_status', n.get_str_value()),
            "isMissedCallFollowUp": lambda n : setattr(self, 'is_missed_call_follow_up', n.get_bool_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "outcome": lambda n : setattr(self, 'outcome', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "relatedCallEventId": lambda n : setattr(self, 'related_call_event_id', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "taskDueAt": lambda n : setattr(self, 'task_due_at', n.get_datetime_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_datetime_value("appointmentEndAt", self.appointment_end_at)
        writer.write_str_value("appointmentNotes", self.appointment_notes)
        writer.write_datetime_value("appointmentStartAt", self.appointment_start_at)
        writer.write_str_value("assignedToUserId", self.assigned_to_user_id)
        writer.write_datetime_value("callbackAt", self.callback_at)
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("changeSource", self.change_source)
        writer.write_str_value("changedByAutomationId", self.changed_by_automation_id)
        writer.write_str_value("followUpStatus", self.follow_up_status)
        writer.write_bool_value("isMissedCallFollowUp", self.is_missed_call_follow_up)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("outcome", self.outcome)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("relatedCallEventId", self.related_call_event_id)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_datetime_value("taskDueAt", self.task_due_at)
        writer.write_datetime_value("timestamp", self.timestamp)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

