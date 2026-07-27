from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone_number_location_coordinate import PhoneNumberLocation_coordinate
    from .phone_number_location_coordinate_source import PhoneNumberLocation_coordinateSource
    from .phone_number_location_time_zone_source import PhoneNumberLocation_timeZoneSource

@dataclass
class PhoneNumberLocation(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for phone number location data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Canonical city resolved by Leadping from its ZIP-code geography data.
    canonical_city: Optional[str] = None
    # Canonical state or territory abbreviation resolved by Leadping.
    canonical_state: Optional[str] = None
    # Latitude and longitude coordinate for this phone number location.
    coordinate: Optional[PhoneNumberLocation_coordinate] = None
    # Describes how the coordinate was resolved.
    coordinate_source: Optional[PhoneNumberLocation_coordinateSource] = None
    # Country code for the phone number or location represented by this phone number location.
    country_code: Optional[str] = None
    # Geographic location metadata for the phone number, lead, or lookup result.
    location: Optional[str] = None
    # State, province, or region for the lead or business postal address.
    state: Optional[str] = None
    # IANA or Windows time zone identifier used for local scheduling and reporting.
    time_zone_id: Optional[str] = None
    # Describes how the time zone was resolved.
    time_zone_source: Optional[PhoneNumberLocation_timeZoneSource] = None
    
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
        from .phone_number_location_coordinate_source import PhoneNumberLocation_coordinateSource
        from .phone_number_location_time_zone_source import PhoneNumberLocation_timeZoneSource

        from .phone_number_location_coordinate import PhoneNumberLocation_coordinate
        from .phone_number_location_coordinate_source import PhoneNumberLocation_coordinateSource
        from .phone_number_location_time_zone_source import PhoneNumberLocation_timeZoneSource

        fields: dict[str, Callable[[Any], None]] = {
            "canonicalCity": lambda n : setattr(self, 'canonical_city', n.get_str_value()),
            "canonicalState": lambda n : setattr(self, 'canonical_state', n.get_str_value()),
            "coordinate": lambda n : setattr(self, 'coordinate', n.get_object_value(PhoneNumberLocation_coordinate)),
            "coordinateSource": lambda n : setattr(self, 'coordinate_source', n.get_object_value(PhoneNumberLocation_coordinateSource)),
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "timeZoneId": lambda n : setattr(self, 'time_zone_id', n.get_str_value()),
            "timeZoneSource": lambda n : setattr(self, 'time_zone_source', n.get_object_value(PhoneNumberLocation_timeZoneSource)),
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
        writer.write_str_value("canonicalCity", self.canonical_city)
        writer.write_str_value("canonicalState", self.canonical_state)
        writer.write_object_value("coordinate", self.coordinate)
        writer.write_object_value("coordinateSource", self.coordinate_source)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_str_value("location", self.location)
        writer.write_str_value("state", self.state)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_object_value("timeZoneSource", self.time_zone_source)
        writer.write_additional_data_value(self.additional_data)
    

