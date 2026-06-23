from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_event_record_state import PhoneNumberEventRecord_state

@dataclass
class PhoneNumberEventRecord(AdditionalDataHolder, Parsable):
    """
    API DTO containing phone number event record data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actor ID associated with this phone number event record.
    actor_id: Optional[str] = None
    # The actor name value for this phone number event record.
    actor_name: Optional[str] = None
    # The date and time for the created at value on this phone number event record.
    created_at: Optional[datetime.datetime] = None
    # The details value for this phone number event record.
    details: Optional[str] = None
    # The unique ID for this phone number event record.
    id: Optional[str] = None
    # Leadping-owned inventory state for phone-number assignment and routing.
    state: Optional[PhoneNumberEventRecord_state] = None
    # The title value for this phone number event record.
    title: Optional[str] = None
    # The type classification for this phone number event record.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberEventRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberEventRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberEventRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_event_record_state import PhoneNumberEventRecord_state

        from .phone_number_event_record_state import PhoneNumberEventRecord_state

        fields: dict[str, Callable[[Any], None]] = {
            "actorId": lambda n : setattr(self, 'actor_id', n.get_str_value()),
            "actorName": lambda n : setattr(self, 'actor_name', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "details": lambda n : setattr(self, 'details', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(PhoneNumberEventRecord_state)),
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
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("details", self.details)
        writer.write_str_value("id", self.id)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("title", self.title)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

