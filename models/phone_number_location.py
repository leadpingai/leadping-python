from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_location_coordinate import PhoneNumberLocation_coordinate

@dataclass
class PhoneNumberLocation(AdditionalDataHolder, Parsable):
    """
    API DTO containing phone number location data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The coordinate inferred for this phone number location.
    coordinate: Optional[PhoneNumberLocation_coordinate] = None
    # The country code value for this phone number location.
    country_code: Optional[str] = None
    # The location value for this phone number location.
    location: Optional[str] = None
    # The current state for this phone number location.
    state: Optional[str] = None
    # The IANA time zone identifier inferred for this phone number location.
    time_zone_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneNumberLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneNumberLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneNumberLocation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone_number_location_coordinate import PhoneNumberLocation_coordinate

        from .phone_number_location_coordinate import PhoneNumberLocation_coordinate

        fields: dict[str, Callable[[Any], None]] = {
            "coordinate": lambda n : setattr(self, 'coordinate', n.get_object_value(PhoneNumberLocation_coordinate)),
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "timeZoneId": lambda n : setattr(self, 'time_zone_id', n.get_str_value()),
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
        writer.write_object_value("coordinate", self.coordinate)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_str_value("location", self.location)
        writer.write_str_value("state", self.state)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_additional_data_value(self.additional_data)
    

