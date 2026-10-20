from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_profile_gender import LeadProfile_gender
    from .lead_profile_qualification import LeadProfile_qualification

@dataclass
class LeadProfile(AdditionalDataHolder, Parsable):
    """
    Public Leadping API schema for lead demographic profile data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Lead birth date used for demographic matching and insurance intake workflows.
    birth_date: Optional[datetime.date] = None
    # Classifies a lead's self-reported gender when required by a qualification, demographic, or integration workflow.
    gender: Optional[LeadProfile_gender] = None
    # Optional consumer qualification details for workflows that need them.
    qualification: Optional[LeadProfile_qualification] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_profile_gender import LeadProfile_gender
        from .lead_profile_qualification import LeadProfile_qualification

        from .lead_profile_gender import LeadProfile_gender
        from .lead_profile_qualification import LeadProfile_qualification

        fields: dict[str, Callable[[Any], None]] = {
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_date_value()),
            "gender": lambda n : setattr(self, 'gender', n.get_enum_value(LeadProfile_gender)),
            "qualification": lambda n : setattr(self, 'qualification', n.get_object_value(LeadProfile_qualification)),
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
        writer.write_date_value("birthDate", self.birth_date)
        writer.write_enum_value("gender", self.gender)
        writer.write_object_value("qualification", self.qualification)
        writer.write_additional_data_value(self.additional_data)
    

