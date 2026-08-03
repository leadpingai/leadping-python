from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PhoneLookupPortability(AdditionalDataHolder, Parsable):
    """
    Number-portability and routing data returned by Telnyx.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Name of the carrier associated with the alternative service provider identifier.
    alternative_carrier_name: Optional[str] = None
    # Carrier type associated with the alternative service provider identifier.
    alternative_carrier_type: Optional[str] = None
    # Alternative service provider identifier reported for the number.
    alternative_spid: Optional[str] = None
    # Name of the carrier currently serving the number.
    carrier_name: Optional[str] = None
    # Type of carrier currently serving the number.
    carrier_type: Optional[str] = None
    # City reported by the portability lookup.
    city: Optional[str] = None
    # Provider-native line type reported by the portability lookup.
    line_type: Optional[str] = None
    # Local routing number used to route calls for the ported number.
    local_routing_number: Optional[str] = None
    # Operating company number associated with the phone number.
    operating_company_number: Optional[str] = None
    # Date on which the phone number was ported, as reported by the provider.
    ported_date: Optional[str] = None
    # Current number-portability status reported by the provider.
    ported_status: Optional[str] = None
    # Service provider identifier currently associated with the number.
    spid: Optional[str] = None
    # State or region reported by the portability lookup.
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneLookupPortability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneLookupPortability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneLookupPortability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "alternativeCarrierName": lambda n : setattr(self, 'alternative_carrier_name', n.get_str_value()),
            "alternativeCarrierType": lambda n : setattr(self, 'alternative_carrier_type', n.get_str_value()),
            "alternativeSpid": lambda n : setattr(self, 'alternative_spid', n.get_str_value()),
            "carrierName": lambda n : setattr(self, 'carrier_name', n.get_str_value()),
            "carrierType": lambda n : setattr(self, 'carrier_type', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "lineType": lambda n : setattr(self, 'line_type', n.get_str_value()),
            "localRoutingNumber": lambda n : setattr(self, 'local_routing_number', n.get_str_value()),
            "operatingCompanyNumber": lambda n : setattr(self, 'operating_company_number', n.get_str_value()),
            "portedDate": lambda n : setattr(self, 'ported_date', n.get_str_value()),
            "portedStatus": lambda n : setattr(self, 'ported_status', n.get_str_value()),
            "spid": lambda n : setattr(self, 'spid', n.get_str_value()),
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
        writer.write_str_value("alternativeCarrierName", self.alternative_carrier_name)
        writer.write_str_value("alternativeCarrierType", self.alternative_carrier_type)
        writer.write_str_value("alternativeSpid", self.alternative_spid)
        writer.write_str_value("carrierName", self.carrier_name)
        writer.write_str_value("carrierType", self.carrier_type)
        writer.write_str_value("city", self.city)
        writer.write_str_value("lineType", self.line_type)
        writer.write_str_value("localRoutingNumber", self.local_routing_number)
        writer.write_str_value("operatingCompanyNumber", self.operating_company_number)
        writer.write_str_value("portedDate", self.ported_date)
        writer.write_str_value("portedStatus", self.ported_status)
        writer.write_str_value("spid", self.spid)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

