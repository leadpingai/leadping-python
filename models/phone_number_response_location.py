from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_location import PhoneNumberLocation

from .phone_number_location import PhoneNumberLocation

@dataclass
class PhoneNumberResponse_location(PhoneNumberLocation, Parsable):
    """
    Geographic location metadata for the phone number, lead, or lookup result.
    """
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberResponse_location:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberResponse_location
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberResponse_location()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_location import PhoneNumberLocation

        from .phone_number_location import PhoneNumberLocation

        fields: dict[str, Callable[[Any], None]] = {
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

