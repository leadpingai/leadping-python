from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AppointmentActivity(AdditionalDataHolder, Parsable):
    """
    An immutable snapshot of an appointment change and its actor.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actorId property
    actor_id: Optional[str] = None
    # The actorName property
    actor_name: Optional[str] = None
    # The assignedToName property
    assigned_to_name: Optional[str] = None
    # The at property
    at: Optional[datetime.datetime] = None
    # The notes property
    notes: Optional[str] = None
    # The reminderAt property
    reminder_at: Optional[datetime.datetime] = None
    # The revision property
    revision: Optional[int] = None
    # The startAt property
    start_at: Optional[datetime.datetime] = None
    # The title property
    title: Optional[str] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppointmentActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppointmentActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppointmentActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actorId": lambda n : setattr(self, 'actor_id', n.get_str_value()),
            "actorName": lambda n : setattr(self, 'actor_name', n.get_str_value()),
            "assignedToName": lambda n : setattr(self, 'assigned_to_name', n.get_str_value()),
            "at": lambda n : setattr(self, 'at', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "reminderAt": lambda n : setattr(self, 'reminder_at', n.get_datetime_value()),
            "revision": lambda n : setattr(self, 'revision', n.get_int_value()),
            "startAt": lambda n : setattr(self, 'start_at', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("actorId", self.actor_id)
        writer.write_str_value("actorName", self.actor_name)
        writer.write_str_value("assignedToName", self.assigned_to_name)
        writer.write_datetime_value("at", self.at)
        writer.write_str_value("notes", self.notes)
        writer.write_datetime_value("reminderAt", self.reminder_at)
        writer.write_int_value("revision", self.revision)
        writer.write_datetime_value("startAt", self.start_at)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

