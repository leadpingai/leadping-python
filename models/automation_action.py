from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_action_settings import AutomationAction_settings

@dataclass
class AutomationAction(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for automation action data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique Leadping identifier for this automation action.
    id: Optional[str] = None
    # Indicates whether this automation action is active and allowed to run.
    is_enabled: Optional[bool] = None
    # Sort order used to evaluate or display this automation action.
    order: Optional[int] = None
    # Key-value settings that configure how this automation action behaves.
    settings: Optional[AutomationAction_settings] = None
    # Type classification used to route and interpret this automation action in the Leadping API.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_action_settings import AutomationAction_settings

        from .automation_action_settings import AutomationAction_settings

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(AutomationAction_settings)),
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
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_int_value("order", self.order)
        writer.write_object_value("settings", self.settings)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

