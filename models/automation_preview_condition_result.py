from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationPreviewConditionResult(AdditionalDataHolder, Parsable):
    """
    Result schema for the Leadping API automation preview condition result returned by lookup and validation endpoints.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Automation condition ID evaluated by this preview result.
    condition_id: Optional[str] = None
    # Indicates whether this automation preview condition result passed the preview or validation check.
    passed: Optional[bool] = None
    # Short human-readable summary of this automation preview condition result for lists, timelines, and notifications.
    summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationPreviewConditionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationPreviewConditionResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationPreviewConditionResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "conditionId": lambda n : setattr(self, 'condition_id', n.get_str_value()),
            "passed": lambda n : setattr(self, 'passed', n.get_bool_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
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
        writer.write_str_value("conditionId", self.condition_id)
        writer.write_bool_value("passed", self.passed)
        writer.write_str_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    

