from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_update_request_compliance import ComplianceUpdateRequest_compliance

@dataclass
class ComplianceUpdateRequest(AdditionalDataHolder, Parsable):
    """
    Request payload for compliance update.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The compliance value for this compliance update.
    compliance: Optional[ComplianceUpdateRequest_compliance] = None
    # The source value for this compliance update.
    source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComplianceUpdateRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComplianceUpdateRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComplianceUpdateRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_update_request_compliance import ComplianceUpdateRequest_compliance

        from .compliance_update_request_compliance import ComplianceUpdateRequest_compliance

        fields: dict[str, Callable[[Any], None]] = {
            "compliance": lambda n : setattr(self, 'compliance', n.get_object_value(ComplianceUpdateRequest_compliance)),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_object_value("compliance", self.compliance)
        writer.write_str_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

