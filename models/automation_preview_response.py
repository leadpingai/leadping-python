from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automation_preview_action_result import AutomationPreviewActionResult
    from .automation_preview_condition_result import AutomationPreviewConditionResult
    from .automation_preview_response_sample_payload import AutomationPreviewResponse_samplePayload
    from .automation_validation_result import AutomationValidationResult

@dataclass
class AutomationPreviewResponse(AdditionalDataHolder, Parsable):
    """
    Response schema for the Leadping API automation preview response returned to authenticated clients.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Action preview results showing what the automation would do.
    action_results: Optional[list[AutomationPreviewActionResult]] = None
    # Condition evaluation results returned by the automation preview.
    condition_results: Optional[list[AutomationPreviewConditionResult]] = None
    # Example payload clients can use to understand this automation preview response format.
    sample_payload: Optional[AutomationPreviewResponse_samplePayload] = None
    # Automation trigger type that starts the workflow.
    trigger_type: Optional[str] = None
    # Validation result returned for the automation configuration.
    validation: Optional[AutomationValidationResult] = None
    # Warnings returned for this automation preview response that do not necessarily block processing.
    warnings: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationPreviewResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationPreviewResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationPreviewResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .automation_preview_action_result import AutomationPreviewActionResult
        from .automation_preview_condition_result import AutomationPreviewConditionResult
        from .automation_preview_response_sample_payload import AutomationPreviewResponse_samplePayload
        from .automation_validation_result import AutomationValidationResult

        from .automation_preview_action_result import AutomationPreviewActionResult
        from .automation_preview_condition_result import AutomationPreviewConditionResult
        from .automation_preview_response_sample_payload import AutomationPreviewResponse_samplePayload
        from .automation_validation_result import AutomationValidationResult

        fields: dict[str, Callable[[Any], None]] = {
            "actionResults": lambda n : setattr(self, 'action_results', n.get_collection_of_object_values(AutomationPreviewActionResult)),
            "conditionResults": lambda n : setattr(self, 'condition_results', n.get_collection_of_object_values(AutomationPreviewConditionResult)),
            "samplePayload": lambda n : setattr(self, 'sample_payload', n.get_object_value(AutomationPreviewResponse_samplePayload)),
            "triggerType": lambda n : setattr(self, 'trigger_type', n.get_str_value()),
            "validation": lambda n : setattr(self, 'validation', n.get_object_value(AutomationValidationResult)),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("actionResults", self.action_results)
        writer.write_collection_of_object_values("conditionResults", self.condition_results)
        writer.write_object_value("samplePayload", self.sample_payload)
        writer.write_str_value("triggerType", self.trigger_type)
        writer.write_object_value("validation", self.validation)
        writer.write_collection_of_primitive_values("warnings", self.warnings)
        writer.write_additional_data_value(self.additional_data)
    

