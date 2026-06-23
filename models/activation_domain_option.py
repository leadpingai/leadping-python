from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ActivationDomainOption(AdditionalDataHolder, Parsable):
    """
    API DTO containing activation domain option data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The current availability status for this activation domain option.
    availability_status: Optional[str] = None
    # The domain name associated with this activation domain option.
    domain_name: Optional[str] = None
    # The industry relevance value for this activation domain option.
    industry_relevance: Optional[str] = None
    # Whether this activation domain option is recommended.
    recommended: Optional[bool] = None
    # The trust concerns value for this activation domain option.
    trust_concerns: Optional[str] = None
    # The why it fits value for this activation domain option.
    why_it_fits: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivationDomainOption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivationDomainOption
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActivationDomainOption()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "availabilityStatus": lambda n : setattr(self, 'availability_status', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "industryRelevance": lambda n : setattr(self, 'industry_relevance', n.get_str_value()),
            "recommended": lambda n : setattr(self, 'recommended', n.get_bool_value()),
            "trustConcerns": lambda n : setattr(self, 'trust_concerns', n.get_str_value()),
            "whyItFits": lambda n : setattr(self, 'why_it_fits', n.get_str_value()),
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
        writer.write_str_value("availabilityStatus", self.availability_status)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("industryRelevance", self.industry_relevance)
        writer.write_bool_value("recommended", self.recommended)
        writer.write_str_value("trustConcerns", self.trust_concerns)
        writer.write_str_value("whyItFits", self.why_it_fits)
        writer.write_additional_data_value(self.additional_data)
    

