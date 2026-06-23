from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .notification_priority import NotificationPriority
    from .notification_type import NotificationType

@dataclass
class NotificationTableRow(AdditionalDataHolder, Parsable):
    """
    API response containing notification data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action button text value for this notification.
    action_button_text: Optional[str] = None
    # The URL associated with this notification.
    action_url: Optional[str] = None
    # The date and time when the entity was created.
    created_at: Optional[datetime.datetime] = None
    # The details value for this notification.
    details: Optional[str] = None
    # The unique identifier for the entity.
    id: Optional[str] = None
    # Whether this notification is read.
    is_read: Optional[bool] = None
    # The message value for this notification.
    message: Optional[str] = None
    # The date and time when the entity was last modified, if applicable.
    modified_at: Optional[datetime.datetime] = None
    # The display name for the entity.
    name: Optional[str] = None
    # The priority value for this notification.
    priority: Optional[NotificationPriority] = None
    # The date and time for the read at value on this notification.
    read_at: Optional[datetime.datetime] = None
    # The related entity ID associated with this notification.
    related_entity_id: Optional[str] = None
    # The related entity type classification for this notification.
    related_entity_type: Optional[str] = None
    # The type classification for this notification.
    type: Optional[NotificationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NotificationTableRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NotificationTableRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NotificationTableRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .notification_priority import NotificationPriority
        from .notification_type import NotificationType

        from .notification_priority import NotificationPriority
        from .notification_type import NotificationType

        fields: dict[str, Callable[[Any], None]] = {
            "actionButtonText": lambda n : setattr(self, 'action_button_text', n.get_str_value()),
            "actionUrl": lambda n : setattr(self, 'action_url', n.get_str_value()),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "details": lambda n : setattr(self, 'details', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isRead": lambda n : setattr(self, 'is_read', n.get_bool_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(NotificationPriority)),
            "readAt": lambda n : setattr(self, 'read_at', n.get_datetime_value()),
            "relatedEntityId": lambda n : setattr(self, 'related_entity_id', n.get_str_value()),
            "relatedEntityType": lambda n : setattr(self, 'related_entity_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(NotificationType)),
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
        writer.write_str_value("actionButtonText", self.action_button_text)
        writer.write_str_value("actionUrl", self.action_url)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("details", self.details)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isRead", self.is_read)
        writer.write_str_value("message", self.message)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("priority", self.priority)
        writer.write_datetime_value("readAt", self.read_at)
        writer.write_str_value("relatedEntityId", self.related_entity_id)
        writer.write_str_value("relatedEntityType", self.related_entity_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

