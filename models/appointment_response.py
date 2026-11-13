from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .appointment_activity import AppointmentActivity

@dataclass
class AppointmentResponse(AdditionalDataHolder, Parsable):
    """
    An appointment visible to the current user, with history populated on detail requests.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignedToName property
    assigned_to_name: Optional[str] = None
    # The assignedToUserId property
    assigned_to_user_id: Optional[str] = None
    # The createdAt property
    created_at: Optional[datetime.datetime] = None
    # The dismissedAt property
    dismissed_at: Optional[datetime.datetime] = None
    # The history property
    history: Optional[list[AppointmentActivity]] = None
    # The id property
    id: Optional[str] = None
    # The isDemo property
    is_demo: Optional[bool] = None
    # The leadAvatarUrl property
    lead_avatar_url: Optional[str] = None
    # The leadEmail property
    lead_email: Optional[str] = None
    # The leadFirstName property
    lead_first_name: Optional[str] = None
    # The leadId property
    lead_id: Optional[str] = None
    # The leadLastName property
    lead_last_name: Optional[str] = None
    # The leadName property
    lead_name: Optional[str] = None
    # The modifiedAt property
    modified_at: Optional[datetime.datetime] = None
    # The notes property
    notes: Optional[str] = None
    # The organizationId property
    organization_id: Optional[str] = None
    # The organizationName property
    organization_name: Optional[str] = None
    # The reminderAt property
    reminder_at: Optional[datetime.datetime] = None
    # The revision property
    revision: Optional[int] = None
    # The startAt property
    start_at: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # The timeZoneId property
    time_zone_id: Optional[str] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppointmentResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppointmentResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppointmentResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .appointment_activity import AppointmentActivity

        from .appointment_activity import AppointmentActivity

        fields: dict[str, Callable[[Any], None]] = {
            "assignedToName": lambda n : setattr(self, 'assigned_to_name', n.get_str_value()),
            "assignedToUserId": lambda n : setattr(self, 'assigned_to_user_id', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "dismissedAt": lambda n : setattr(self, 'dismissed_at', n.get_datetime_value()),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(AppointmentActivity)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isDemo": lambda n : setattr(self, 'is_demo', n.get_bool_value()),
            "leadAvatarUrl": lambda n : setattr(self, 'lead_avatar_url', n.get_str_value()),
            "leadEmail": lambda n : setattr(self, 'lead_email', n.get_str_value()),
            "leadFirstName": lambda n : setattr(self, 'lead_first_name', n.get_str_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "leadLastName": lambda n : setattr(self, 'lead_last_name', n.get_str_value()),
            "leadName": lambda n : setattr(self, 'lead_name', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "organizationId": lambda n : setattr(self, 'organization_id', n.get_str_value()),
            "organizationName": lambda n : setattr(self, 'organization_name', n.get_str_value()),
            "reminderAt": lambda n : setattr(self, 'reminder_at', n.get_datetime_value()),
            "revision": lambda n : setattr(self, 'revision', n.get_int_value()),
            "startAt": lambda n : setattr(self, 'start_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "timeZoneId": lambda n : setattr(self, 'time_zone_id', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("assignedToName", self.assigned_to_name)
        writer.write_str_value("assignedToUserId", self.assigned_to_user_id)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_datetime_value("dismissedAt", self.dismissed_at)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isDemo", self.is_demo)
        writer.write_str_value("leadAvatarUrl", self.lead_avatar_url)
        writer.write_str_value("leadEmail", self.lead_email)
        writer.write_str_value("leadFirstName", self.lead_first_name)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("leadLastName", self.lead_last_name)
        writer.write_str_value("leadName", self.lead_name)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("organizationId", self.organization_id)
        writer.write_str_value("organizationName", self.organization_name)
        writer.write_datetime_value("reminderAt", self.reminder_at)
        writer.write_int_value("revision", self.revision)
        writer.write_datetime_value("startAt", self.start_at)
        writer.write_str_value("status", self.status)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

