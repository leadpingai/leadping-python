from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_availability_response_location import PhoneNumberAvailabilityResponse_location

@dataclass
class PhoneNumberAvailabilityResponse(AdditionalDataHolder, Parsable):
    """
    API response containing phone number availability data returned to callers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ISO currency code for monetary values in this phone number availability.
    currency: Optional[str] = None
    # Whether this phone number availability is available.
    is_available: Optional[bool] = None
    # The location value for this phone number availability.
    location: Optional[PhoneNumberAvailabilityResponse_location] = None
    # The phone number associated with this phone number availability.
    phone_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberAvailabilityResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberAvailabilityResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberAvailabilityResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_availability_response_location import PhoneNumberAvailabilityResponse_location

        from .phone_number_availability_response_location import PhoneNumberAvailabilityResponse_location

        fields: dict[str, Callable[[Any], None]] = {
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "isAvailable": lambda n : setattr(self, 'is_available', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(PhoneNumberAvailabilityResponse_location)),
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
        writer.write_str_value("currency", self.currency)
        writer.write_bool_value("isAvailable", self.is_available)
        writer.write_object_value("location", self.location)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_additional_data_value(self.additional_data)
    

