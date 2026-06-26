from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_condition import AutomationCondition

@dataclass
class AutomationConditionGroup(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for automation condition group data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Automation conditions evaluated before an action or workflow runs.
    conditions: Optional[list[AutomationCondition]] = None
    # Unique Leadping identifier for this automation condition group.
    id: Optional[str] = None
    # Execution mode that controls how this automation condition group is evaluated.
    mode: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationConditionGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationConditionGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationConditionGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_condition import AutomationCondition

        from .automation_condition import AutomationCondition

        fields: dict[str, Callable[[Any], None]] = {
            "conditions": lambda n : setattr(self, 'conditions', n.get_collection_of_object_values(AutomationCondition)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
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
        writer.write_collection_of_object_values("conditions", self.conditions)
        writer.write_str_value("id", self.id)
        writer.write_str_value("mode", self.mode)
        writer.write_additional_data_value(self.additional_data)
    

