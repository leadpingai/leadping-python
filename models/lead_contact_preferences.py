from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_callback_window import LeadCallbackWindow
    from .lead_contact_preferences_channel import LeadContactPreferences_channel

@dataclass
class LeadContactPreferences(AdditionalDataHolder, Parsable):
    """
    Preferred contact language, channel, and callback windows; does not grant consent.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Preferred callback windows in the contact time zone.
    callback_windows: Optional[list[LeadCallbackWindow]] = None
    # Supported LeadContactChannel values.
    channel: Optional[LeadContactPreferences_channel] = None
    # Preferred BCP 47 language tag, such as en-US.
    language: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadContactPreferences:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadContactPreferences
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadContactPreferences()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_callback_window import LeadCallbackWindow
        from .lead_contact_preferences_channel import LeadContactPreferences_channel

        from .lead_callback_window import LeadCallbackWindow
        from .lead_contact_preferences_channel import LeadContactPreferences_channel

        fields: dict[str, Callable[[Any], None]] = {
            "callbackWindows": lambda n : setattr(self, 'callback_windows', n.get_collection_of_object_values(LeadCallbackWindow)),
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(LeadContactPreferences_channel)),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
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
        writer.write_collection_of_object_values("callbackWindows", self.callback_windows)
        writer.write_enum_value("channel", self.channel)
        writer.write_str_value("language", self.language)
        writer.write_additional_data_value(self.additional_data)
    

