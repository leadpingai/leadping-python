from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class LeadCompany(AdditionalDataHolder, Parsable):
    """
    Business represented by a lead contact.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Number of employees, when known.
    employee_count: Optional[int] = None
    # Industry of the business, independent of the requested service.
    industry: Optional[str] = None
    # Contact role at the business.
    job_title: Optional[str] = None
    # Business name.
    name: Optional[str] = None
    # Business website URL.
    website: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadCompany:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadCompany
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadCompany()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "employeeCount": lambda n : setattr(self, 'employee_count', n.get_int_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_str_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_int_value("employeeCount", self.employee_count)
        writer.write_str_value("industry", self.industry)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("name", self.name)
        writer.write_str_value("website", self.website)
        writer.write_additional_data_value(self.additional_data)
    

