from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_workflow_run_response import AutomationWorkflowRunResponse

@dataclass
class AutomationWorkflowStatusResponse(AdditionalDataHolder, Parsable):
    """
    Automation workflow status collection for a lead.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier of the lead associated with this Leadping automation workflow status.
    lead_id: Optional[str] = None
    # Collection of runs included with this Leadping automation workflow status.
    runs: Optional[list[AutomationWorkflowRunResponse]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationWorkflowStatusResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationWorkflowStatusResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationWorkflowStatusResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_workflow_run_response import AutomationWorkflowRunResponse

        from .automation_workflow_run_response import AutomationWorkflowRunResponse

        fields: dict[str, Callable[[Any], None]] = {
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(AutomationWorkflowRunResponse)),
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
        writer.write_str_value("leadId", self.lead_id)
        writer.write_collection_of_object_values("runs", self.runs)
        writer.write_additional_data_value(self.additional_data)
    

