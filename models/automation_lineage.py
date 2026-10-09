from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationLineage(AdditionalDataHolder, Parsable):
    """
    Persisted origin of an automation run and the events produced by its actions.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The actionId property
    action_id: Optional[str] = None
    # Automation IDs in execution order, including the run that produced this event.
    automation_ids: Optional[list[str]] = None
    # The rootEventId property
    root_event_id: Optional[str] = None
    # The runId property
    run_id: Optional[str] = None
    # The triggerEventId property
    trigger_event_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationLineage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationLineage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationLineage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actionId": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "automationIds": lambda n : setattr(self, 'automation_ids', n.get_collection_of_primitive_values(str)),
            "rootEventId": lambda n : setattr(self, 'root_event_id', n.get_str_value()),
            "runId": lambda n : setattr(self, 'run_id', n.get_str_value()),
            "triggerEventId": lambda n : setattr(self, 'trigger_event_id', n.get_str_value()),
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
        writer.write_str_value("actionId", self.action_id)
        writer.write_collection_of_primitive_values("automationIds", self.automation_ids)
        writer.write_str_value("rootEventId", self.root_event_id)
        writer.write_str_value("runId", self.run_id)
        writer.write_str_value("triggerEventId", self.trigger_event_id)
        writer.write_additional_data_value(self.additional_data)
    

