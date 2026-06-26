from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_search_result_location import PhoneNumberSearchResult_location

@dataclass
class PhoneNumberSearchResult(AdditionalDataHolder, Parsable):
    """
    Result schema for the Leadping API phone number search result returned by lookup and validation endpoints.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Geographic location metadata for the phone number, lead, or lookup result.
    location: Optional[PhoneNumberSearchResult_location] = None
    # E.164 phone number exposed by this phone number search result.
    number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberSearchResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberSearchResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberSearchResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_search_result_location import PhoneNumberSearchResult_location

        from .phone_number_search_result_location import PhoneNumberSearchResult_location

        fields: dict[str, Callable[[Any], None]] = {
            "location": lambda n : setattr(self, 'location', n.get_object_value(PhoneNumberSearchResult_location)),
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
        writer.write_object_value("location", self.location)
        writer.write_str_value("number", self.number)
        writer.write_additional_data_value(self.additional_data)
    

