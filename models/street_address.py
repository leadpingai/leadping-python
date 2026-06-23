from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StreetAddress(AdditionalDataHolder, Parsable):
    """
    A minimal, serializable record type for physical mailing addresses, with support for international formats and compatibility with common APIs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional additional notes or delivery instructions.
    additional_info: Optional[str] = None
    # The city, town, or locality.
    city: Optional[str] = None
    # The ISO 3166-1 alpha-2 country code (e.g., "US", "GB", "CA").
    country: Optional[str] = None
    # The primary address line (e.g., street address, P.O. box, company name).
    line1: Optional[str] = None
    # The secondary address line (e.g., apartment, suite, unit, or building).
    line2: Optional[str] = None
    # The postal or ZIP code.
    postal_code: Optional[str] = None
    # The province or territory, if distinct from state in your use case (optional, use with care).
    province: Optional[str] = None
    # The broader region, district, or administrative area (e.g., prefecture or county).
    region: Optional[str] = None
    # The state, province, or equivalent administrative region. Commonly used in countries like the US, Canada, and Australia.
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StreetAddress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StreetAddress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StreetAddress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "additionalInfo": lambda n : setattr(self, 'additional_info', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "line1": lambda n : setattr(self, 'line1', n.get_str_value()),
            "line2": lambda n : setattr(self, 'line2', n.get_str_value()),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "province": lambda n : setattr(self, 'province', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_str_value("additionalInfo", self.additional_info)
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_str_value("line1", self.line1)
        writer.write_str_value("line2", self.line2)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("province", self.province)
        writer.write_str_value("region", self.region)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

