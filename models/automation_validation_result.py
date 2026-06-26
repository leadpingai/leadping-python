from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationValidationResult(AdditionalDataHolder, Parsable):
    """
    Result schema for the Leadping API automation validation result returned by lookup and validation endpoints.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Validation or processing errors returned for this automation validation result.
    errors: Optional[list[str]] = None
    # Warnings returned for this automation validation result that do not necessarily block processing.
    warnings: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationValidationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationValidationResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationValidationResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("errors", self.errors)
        writer.write_collection_of_primitive_values("warnings", self.warnings)
        writer.write_additional_data_value(self.additional_data)
    

