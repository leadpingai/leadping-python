from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationPreviewActionResult(AdditionalDataHolder, Parsable):
    """
    API DTO containing automation preview action result data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action ID associated with this automation preview action result.
    action_id: Optional[str] = None
    # The rendered output value for this automation preview action result.
    rendered_output: Optional[str] = None
    # The summary value for this automation preview action result.
    summary: Optional[str] = None
    # The warnings included with this automation preview action result.
    warnings: Optional[list[str]] = None
    # Whether this automation preview action result would have side effect.
    would_have_side_effect: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationPreviewActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationPreviewActionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationPreviewActionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "actionId": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "renderedOutput": lambda n : setattr(self, 'rendered_output', n.get_str_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_primitive_values(str)),
            "wouldHaveSideEffect": lambda n : setattr(self, 'would_have_side_effect', n.get_bool_value()),
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
        writer.write_str_value("renderedOutput", self.rendered_output)
        writer.write_str_value("summary", self.summary)
        writer.write_collection_of_primitive_values("warnings", self.warnings)
        writer.write_bool_value("wouldHaveSideEffect", self.would_have_side_effect)
        writer.write_additional_data_value(self.additional_data)
    

