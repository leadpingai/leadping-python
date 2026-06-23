from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_lookup import Phone_lookup

@dataclass
class Phone(AdditionalDataHolder, Parsable):
    """
    API DTO containing phone data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The lookup value for this phone.
    lookup: Optional[Phone_lookup] = None
    # The number value for this phone.
    number: Optional[str] = None
    # The type classification for this phone.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Phone:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Phone
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Phone()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_lookup import Phone_lookup

        from .phone_lookup import Phone_lookup

        fields: dict[str, Callable[[Any], None]] = {
            "lookup": lambda n : setattr(self, 'lookup', n.get_object_value(Phone_lookup)),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_object_value("lookup", self.lookup)
        writer.write_str_value("number", self.number)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

