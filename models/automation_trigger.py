from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_trigger_settings import AutomationTrigger_settings

@dataclass
class AutomationTrigger(AdditionalDataHolder, Parsable):
    """
    API DTO containing automation trigger data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The human-readable display name shown for this automation trigger.
    display_name: Optional[str] = None
    # The unique ID for this automation trigger.
    id: Optional[str] = None
    # Whether this automation trigger is enabled.
    is_enabled: Optional[bool] = None
    # The settings key-value data carried with this automation trigger; values must be safe to expose in API responses.
    settings: Optional[AutomationTrigger_settings] = None
    # The type classification for this automation trigger.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationTrigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationTrigger
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationTrigger()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_trigger_settings import AutomationTrigger_settings

        from .automation_trigger_settings import AutomationTrigger_settings

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(AutomationTrigger_settings)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("settings", self.settings)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

