from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_request_snapshot import AutomationRequestSnapshot

@dataclass
class AutomationPreviewRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API automation preview request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Automation configuration to evaluate without executing live actions.
    automation: Optional[AutomationRequestSnapshot] = None
    # Automation trigger type that starts the workflow.
    trigger_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationPreviewRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationPreviewRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationPreviewRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_request_snapshot import AutomationRequestSnapshot

        from .automation_request_snapshot import AutomationRequestSnapshot

        fields: dict[str, Callable[[Any], None]] = {
            "automation": lambda n : setattr(self, 'automation', n.get_object_value(AutomationRequestSnapshot)),
            "triggerType": lambda n : setattr(self, 'trigger_type', n.get_str_value()),
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
        writer.write_object_value("automation", self.automation)
        writer.write_str_value("triggerType", self.trigger_type)
        writer.write_additional_data_value(self.additional_data)
    

