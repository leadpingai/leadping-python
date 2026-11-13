from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AppointmentRequest(AdditionalDataHolder, Parsable):
    """
    Creates or reschedules an agent's callback appointment.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The assignedToUserId property
    assigned_to_user_id: Optional[str] = None
    # The expectedRevision property
    expected_revision: Optional[int] = None
    # The leadId property
    lead_id: Optional[str] = None
    # The notes property
    notes: Optional[str] = None
    # The startAt property
    start_at: Optional[datetime.datetime] = None
    # The timeZoneId property
    time_zone_id: Optional[str] = None
    # The title property
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppointmentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppointmentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppointmentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignedToUserId": lambda n : setattr(self, 'assigned_to_user_id', n.get_str_value()),
            "expectedRevision": lambda n : setattr(self, 'expected_revision', n.get_int_value()),
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "startAt": lambda n : setattr(self, 'start_at', n.get_datetime_value()),
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
        writer.write_str_value("assignedToUserId", self.assigned_to_user_id)
        writer.write_int_value("expectedRevision", self.expected_revision)
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("notes", self.notes)
        writer.write_datetime_value("startAt", self.start_at)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

