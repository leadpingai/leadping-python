from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .customer_activation_health_item import CustomerActivationHealthItem

@dataclass
class CustomerActivationHealth(AdditionalDataHolder, Parsable):
    """
    Represents customer activation health data exposed by Leadping analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of items included with this Leadping customer activation health.
    items: Optional[list[CustomerActivationHealthItem]] = None
    # Current overall status for this Leadping customer activation health.
    overall_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerActivationHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerActivationHealth
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerActivationHealth()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .customer_activation_health_item import CustomerActivationHealthItem

        from .customer_activation_health_item import CustomerActivationHealthItem

        fields: dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(CustomerActivationHealthItem)),
            "overallStatus": lambda n : setattr(self, 'overall_status', n.get_str_value()),
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
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("overallStatus", self.overall_status)
        writer.write_additional_data_value(self.additional_data)
    

