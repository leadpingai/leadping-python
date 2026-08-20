from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_status_change_request_category import LeadStatusChangeRequest_category

@dataclass
class LeadStatusChangeRequest(AdditionalDataHolder, Parsable):
    """
    Defines a lead status transition or correction, including its target status, effective time, source, and explanatory context.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # UTC timestamp for appointment end at on this lead status change.
    appointment_end_at: Optional[datetime.datetime] = None
    # Additional scheduling or preparation notes for the related appointment.
    appointment_notes: Optional[str] = None
    # UTC timestamp for appointment start at on this lead status change.
    appointment_start_at: Optional[datetime.datetime] = None
    # UTC timestamp for callback at on this lead status change.
    callback_at: Optional[datetime.datetime] = None
    # Controlled lead status change categories used for reporting, automation, and analytics.
    category: Optional[LeadStatusChangeRequest_category] = None
    # The current follow up status for this lead status change.
    follow_up_status: Optional[str] = None
    # The operator or customer notes recorded for this lead status change.
    notes: Optional[str] = None
    # Result of the interaction or workflow step that caused the status change.
    outcome: Optional[str] = None
    # The reason this lead status change was changed.
    reason: Optional[str] = None
    # UTC timestamp for task due at on this lead status change.
    task_due_at: Optional[datetime.datetime] = None
    # Category of status change being recorded for the lead.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadStatusChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadStatusChangeRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadStatusChangeRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_status_change_request_category import LeadStatusChangeRequest_category

        from .lead_status_change_request_category import LeadStatusChangeRequest_category

        fields: dict[str, Callable[[Any], None]] = {
            "appointmentEndAt": lambda n : setattr(self, 'appointment_end_at', n.get_datetime_value()),
            "appointmentNotes": lambda n : setattr(self, 'appointment_notes', n.get_str_value()),
            "appointmentStartAt": lambda n : setattr(self, 'appointment_start_at', n.get_datetime_value()),
            "callbackAt": lambda n : setattr(self, 'callback_at', n.get_datetime_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(LeadStatusChangeRequest_category)),
            "followUpStatus": lambda n : setattr(self, 'follow_up_status', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "outcome": lambda n : setattr(self, 'outcome', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "taskDueAt": lambda n : setattr(self, 'task_due_at', n.get_datetime_value()),
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
        writer.write_datetime_value("callbackAt", self.callback_at)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("followUpStatus", self.follow_up_status)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("outcome", self.outcome)
        writer.write_str_value("reason", self.reason)
        writer.write_datetime_value("taskDueAt", self.task_due_at)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

