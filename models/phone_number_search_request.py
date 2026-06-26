from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_search_request_location import PhoneNumberSearchRequest_location

@dataclass
class PhoneNumberSearchRequest(AdditionalDataHolder, Parsable):
    """
    Request schema for the Leadping API phone number search request, including the fields clients can send.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Geographic location metadata for the phone number, lead, or lookup result.
    location: Optional[PhoneNumberSearchRequest_location] = None
    # Phone number used by this phone number search request for calls, SMS, lookup, or routing.
    phone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberSearchRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberSearchRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberSearchRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_search_request_location import PhoneNumberSearchRequest_location

        from .phone_number_search_request_location import PhoneNumberSearchRequest_location

        fields: dict[str, Callable[[Any], None]] = {
            "location": lambda n : setattr(self, 'location', n.get_object_value(PhoneNumberSearchRequest_location)),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
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
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_additional_data_value(self.additional_data)
    

