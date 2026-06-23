from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disposition_export_row_category import DispositionExportRow_category
    from .disposition_export_row_change_source import DispositionExportRow_changeSource

@dataclass
class DispositionExportRow(AdditionalDataHolder, Parsable):
    """
    API response containing disposition export row data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time for the appointment end at value on this disposition export row.
    appointment_end_at: Optional[datetime.datetime] = None
    # The date and time for the appointment start at value on this disposition export row.
    appointment_start_at: Optional[datetime.datetime] = None
    # The assigned to user ID associated with this disposition export row.
    assigned_to_user_id: Optional[str] = None
    # The date and time for the callback at value on this disposition export row.
    callback_at: Optional[datetime.datetime] = None
    # Controlled disposition categories used for reporting, automation, and analytics.
    category: Optional[DispositionExportRow_category] = None
    # Known sources that can change a lead's current disposition.
    change_source: Optional[DispositionExportRow_changeSource] = None
    # The changedAt property
    changed_at: Optional[datetime.datetime] = None
    # The changedByAutomationId property
    changed_by_automation_id: Optional[str] = None
    # The changedByUserId property
    changed_by_user_id: Optional[str] = None
    # The date and time for the created at value on this disposition export row.
    created_at: Optional[datetime.datetime] = None
    # The disposition ID associated with this disposition export row.
    disposition_id: Optional[str] = None
    # The current follow up status for this disposition export row.
    follow_up_status: Optional[str] = None
    # Whether this disposition export row is missed call follow up.
    is_missed_call_follow_up: Optional[bool] = None
    # The lead ID associated with this disposition export row.
    lead_id: Optional[str] = None
    # The newDispositionId property
    new_disposition_id: Optional[str] = None
    # The operator or customer notes recorded for this disposition export row.
    notes: Optional[str] = None
    # The oldDispositionId property
    old_disposition_id: Optional[str] = None
    # The oldDispositionOutcome property
    old_disposition_outcome: Optional[str] = None
    # The oldDispositionType property
    old_disposition_type: Optional[str] = None
    # The outcome value for this disposition export row.
    outcome: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The related call event ID associated with this disposition export row.
    related_call_event_id: Optional[str] = None
    # The source ID associated with this disposition export row.
    source_id: Optional[str] = None
    # The date and time for the task due at value on this disposition export row.
    task_due_at: Optional[datetime.datetime] = None
    # The type classification for this disposition export row.
    type: Optional[str] = None
    # The date and time for the updated at value on this disposition export row.
    updated_at: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispositionExportRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispositionExportRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispositionExportRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .disposition_export_row_category import DispositionExportRow_category
        from .disposition_export_row_change_source import DispositionExportRow_changeSource

        from .disposition_export_row_category import DispositionExportRow_category
        from .disposition_export_row_change_source import DispositionExportRow_changeSource

        fields: dict[str, Callable[[Any], None]] = {
            "appointmentEndAt": lambda n : setattr(self, 'appointment_end_at', n.get_datetime_value()),
            "appointmentStartAt": lambda n : setattr(self, 'appointment_start_at', n.get_datetime_value()),
            "assignedToUserId": lambda n : setattr(self, 'assigned_to_user_id', n.get_str_value()),
            "callbackAt": lambda n : setattr(self, 'callback_at', n.get_datetime_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(DispositionExportRow_category)),
            "changeSource": lambda n : setattr(self, 'change_source', n.get_enum_value(DispositionExportRow_changeSource)),
            "changedAt": lambda n : setattr(self, 'changed_at', n.get_datetime_value()),
            "changedByAutomationId": lambda n : setattr(self, 'changed_by_automation_id', n.get_str_value()),
            "changedByUserId": lambda n : setattr(self, 'changed_by_user_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "dispositionId": lambda n : setattr(self, 'disposition_id', n.get_str_value()),
            "followUpStatus": lambda n : setattr(self, 'follow_up_status', n.get_str_value()),
            "isMissedCallFollowUp": lambda n : setattr(self, 'is_missed_call_follow_up', n.get_bool_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "newDispositionId": lambda n : setattr(self, 'new_disposition_id', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "oldDispositionId": lambda n : setattr(self, 'old_disposition_id', n.get_str_value()),
            "oldDispositionOutcome": lambda n : setattr(self, 'old_disposition_outcome', n.get_str_value()),
            "oldDispositionType": lambda n : setattr(self, 'old_disposition_type', n.get_str_value()),
            "outcome": lambda n : setattr(self, 'outcome', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "relatedCallEventId": lambda n : setattr(self, 'related_call_event_id', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "taskDueAt": lambda n : setattr(self, 'task_due_at', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "updatedAt": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
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
        writer.write_datetime_value("appointmentStartAt", self.appointment_start_at)
        writer.write_str_value("assignedToUserId", self.assigned_to_user_id)
        writer.write_datetime_value("callbackAt", self.callback_at)
        writer.write_enum_value("category", self.category)
        writer.write_enum_value("changeSource", self.change_source)
        writer.write_datetime_value("changedAt", self.changed_at)
        writer.write_str_value("changedByAutomationId", self.changed_by_automation_id)
        writer.write_str_value("changedByUserId", self.changed_by_user_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("dispositionId", self.disposition_id)
        writer.write_str_value("followUpStatus", self.follow_up_status)
        writer.write_bool_value("isMissedCallFollowUp", self.is_missed_call_follow_up)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("newDispositionId", self.new_disposition_id)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("oldDispositionId", self.old_disposition_id)
        writer.write_str_value("oldDispositionOutcome", self.old_disposition_outcome)
        writer.write_str_value("oldDispositionType", self.old_disposition_type)
        writer.write_str_value("outcome", self.outcome)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("relatedCallEventId", self.related_call_event_id)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_datetime_value("taskDueAt", self.task_due_at)
        writer.write_str_value("type", self.type)
        writer.write_datetime_value("updatedAt", self.updated_at)
        writer.write_additional_data_value(self.additional_data)
    

