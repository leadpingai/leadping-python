from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_status_request_category import LeadStatusRequest_category

@dataclass
class LeadStatusRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Controlled disposition categories used for reporting, automation, and analytics.
    category: Optional[LeadStatusRequest_category] = None
    # The color property
    color: Optional[str] = None
    # The name property
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadStatusRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadStatusRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadStatusRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_status_request_category import LeadStatusRequest_category

        from .lead_status_request_category import LeadStatusRequest_category

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(LeadStatusRequest_category)),
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("color", self.color)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

