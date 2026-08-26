from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutomationConnection(AdditionalDataHolder, Parsable):
    """
    A directed connection between two nodes in an automation graph.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique identifier for this connection.
    id: Optional[str] = None
    # Graph node identifier where the connection begins.
    source_node_id: Optional[str] = None
    # Graph node identifier where the connection ends.
    target_node_id: Optional[str] = None
    # Percentage chance assigned to this connection when it leaves a weighted random split. Ignored for connections from other node types.
    weight: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomationConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomationConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomationConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "sourceNodeId": lambda n : setattr(self, 'source_node_id', n.get_str_value()),
            "targetNodeId": lambda n : setattr(self, 'target_node_id', n.get_str_value()),
            "weight": lambda n : setattr(self, 'weight', n.get_int_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("sourceNodeId", self.source_node_id)
        writer.write_str_value("targetNodeId", self.target_node_id)
        writer.write_int_value("weight", self.weight)
        writer.write_additional_data_value(self.additional_data)
    

