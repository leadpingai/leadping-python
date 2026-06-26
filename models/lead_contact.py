from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_contact_coordinate import LeadContact_coordinate
    from .lead_contact_phone import LeadContact_phone
    from .lead_contact_street_address import LeadContact_streetAddress

@dataclass
class LeadContact(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for lead contact profile data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Latitude and longitude coordinate for this lead contact profile.
    coordinate: Optional[LeadContact_coordinate] = None
    # Email address for the person represented by this lead contact profile.
    email: Optional[str] = None
    # First name of the lead, user, or contact represented by this lead contact profile.
    first_name: Optional[str] = None
    # Last name of the lead, user, or contact represented by this lead contact profile.
    last_name: Optional[str] = None
    # Phone details for the lead, user, or business represented by this lead contact profile.
    phone: Optional[LeadContact_phone] = None
    # Postal street address for the lead contact profile.
    street_address: Optional[LeadContact_streetAddress] = None
    # IANA or Windows time zone identifier used for local scheduling and reporting.
    time_zone_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadContact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadContact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadContact()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_contact_coordinate import LeadContact_coordinate
        from .lead_contact_phone import LeadContact_phone
        from .lead_contact_street_address import LeadContact_streetAddress

        from .lead_contact_coordinate import LeadContact_coordinate
        from .lead_contact_phone import LeadContact_phone
        from .lead_contact_street_address import LeadContact_streetAddress

        fields: dict[str, Callable[[Any], None]] = {
            "coordinate": lambda n : setattr(self, 'coordinate', n.get_object_value(LeadContact_coordinate)),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_object_value(LeadContact_phone)),
            "streetAddress": lambda n : setattr(self, 'street_address', n.get_object_value(LeadContact_streetAddress)),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_object_value("phone", self.phone)
        writer.write_object_value("streetAddress", self.street_address)
        writer.write_str_value("timeZoneId", self.time_zone_id)
        writer.write_additional_data_value(self.additional_data)
    

