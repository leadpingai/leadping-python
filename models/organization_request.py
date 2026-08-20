from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organization_request_address import OrganizationRequest_address

@dataclass
class OrganizationRequest(AdditionalDataHolder, Parsable):
    """
    Defines the fields clients can send when working with organization profile.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Postal address for the organization, lead, or contact represented by this organization profile request.
    address: Optional[OrganizationRequest_address] = None
    # Human-readable description that explains this organization profile request to API users.
    description: Optional[str] = None
    # Employer Identification Number used for organization and 10DLC verification.
    ein: Optional[str] = None
    # Whether the organization was formed less than 90 days ago.
    is_younger_than90: Optional[bool] = None
    # Primary organization name.
    name: Optional[str] = None
    # Phone details for the lead, user, or organization represented by this organization profile request.
    phone: Optional[str] = None
    # Alternate organization name or DBA shown in Leadping.
    secondary_name: Optional[str] = None
    # Industry vertical used for lead routing, compliance review, and reporting.
    vertical: Optional[str] = None
    # Organization website URL used for compliance, brand review, and lead attribution.
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrganizationRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .organization_request_address import OrganizationRequest_address

        from .organization_request_address import OrganizationRequest_address

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(OrganizationRequest_address)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "ein": lambda n : setattr(self, 'ein', n.get_str_value()),
            "isYoungerThan90": lambda n : setattr(self, 'is_younger_than90', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "secondaryName": lambda n : setattr(self, 'secondary_name', n.get_str_value()),
            "vertical": lambda n : setattr(self, 'vertical', n.get_str_value()),
            "website": lambda n : setattr(self, 'website', n.get_str_value()),
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
        writer.write_object_value("address", self.address)
        writer.write_str_value("description", self.description)
        writer.write_str_value("ein", self.ein)
        writer.write_bool_value("isYoungerThan90", self.is_younger_than90)
        writer.write_str_value("name", self.name)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("secondaryName", self.secondary_name)
        writer.write_str_value("vertical", self.vertical)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

