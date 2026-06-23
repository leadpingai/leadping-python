from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_lookup_carrier_type import PhoneLookup_carrierType
    from .phone_lookup_line_type import PhoneLookup_lineType
    from .phone_lookup_location import PhoneLookup_location

@dataclass
class PhoneLookup(AdditionalDataHolder, Parsable):
    """
    Represents phone information retrieved from a phone number lookup
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An enumerator describing carrier types
    carrier_type: Optional[PhoneLookup_carrierType] = None
    # Gets or sets created at.
    created_at: Optional[datetime.datetime] = None
    # Gets or sets id.
    id: Optional[str] = None
    # Whether this phone lookup is valid.
    is_valid: Optional[bool] = None
    # An enumerator describing phone line types
    line_type: Optional[PhoneLookup_lineType] = None
    # The location value for this phone lookup.
    location: Optional[PhoneLookup_location] = None
    # Gets or sets modified at.
    modified_at: Optional[datetime.datetime] = None
    # The number value for this phone lookup.
    number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneLookup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneLookup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneLookup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_lookup_carrier_type import PhoneLookup_carrierType
        from .phone_lookup_line_type import PhoneLookup_lineType
        from .phone_lookup_location import PhoneLookup_location

        from .phone_lookup_carrier_type import PhoneLookup_carrierType
        from .phone_lookup_line_type import PhoneLookup_lineType
        from .phone_lookup_location import PhoneLookup_location

        fields: dict[str, Callable[[Any], None]] = {
            "carrierType": lambda n : setattr(self, 'carrier_type', n.get_enum_value(PhoneLookup_carrierType)),
            "createdAt": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isValid": lambda n : setattr(self, 'is_valid', n.get_bool_value()),
            "lineType": lambda n : setattr(self, 'line_type', n.get_enum_value(PhoneLookup_lineType)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(PhoneLookup_location)),
            "modifiedAt": lambda n : setattr(self, 'modified_at', n.get_datetime_value()),
            "number": lambda n : setattr(self, 'number', n.get_str_value()),
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
        writer.write_enum_value("carrierType", self.carrier_type)
        writer.write_datetime_value("createdAt", self.created_at)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isValid", self.is_valid)
        writer.write_enum_value("lineType", self.line_type)
        writer.write_object_value("location", self.location)
        writer.write_datetime_value("modifiedAt", self.modified_at)
        writer.write_str_value("number", self.number)
        writer.write_additional_data_value(self.additional_data)
    

