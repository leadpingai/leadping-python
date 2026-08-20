from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_request_notification_preferences import UserRequest_notificationPreferences

@dataclass
class UserRequest(AdditionalDataHolder, Parsable):
    """
    Defines the fields clients can send when working with user profile.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # First name of the lead, user, or contact represented by this user profile request.
    first_name: Optional[str] = None
    # Last name of the lead, user, or contact represented by this user profile request.
    last_name: Optional[str] = None
    # Display name for the user.
    name: Optional[str] = None
    # Notification preferences configured for the user.
    notification_preferences: Optional[UserRequest_notificationPreferences] = None
    # Phone details for the lead, user, or organization represented by this user profile request.
    phone: Optional[str] = None
    # IANA time zone identifier used when displaying dates and times for this user.
    time_zone_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_request_notification_preferences import UserRequest_notificationPreferences

        from .user_request_notification_preferences import UserRequest_notificationPreferences

        fields: dict[str, Callable[[Any], None]] = {
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "notificationPreferences": lambda n : setattr(self, 'notification_preferences', n.get_object_value(UserRequest_notificationPreferences)),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "timeZoneId": lambda n : setattr(self, 'time_zone_id', n.get_str_value()),
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
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("name", self.name)
        writer.write_object_value("notificationPreferences", self.notification_preferences)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_additional_data_value(self.additional_data)
    

