from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_profile_employment_type import LeadProfile_employmentType
    from .lead_profile_gender import LeadProfile_gender
    from .lead_profile_marital_status import LeadProfile_maritalStatus

@dataclass
class LeadProfile(AdditionalDataHolder, Parsable):
    """
    API DTO containing lead profile data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The date and time for the birth date value on this lead profile.
    birth_date: Optional[datetime.date] = None
    # Defines the supported Employment Type values.
    employment_type: Optional[LeadProfile_employmentType] = None
    # Represents a gender classification used for demographic or identification purposes.
    gender: Optional[LeadProfile_gender] = None
    # Whether this lead profile has bankruptcy.
    has_bankruptcy: Optional[bool] = None
    # Whether this lead profile has medical condition.
    has_medical_condition: Optional[bool] = None
    # Whether this lead profile is homeowner.
    is_homeowner: Optional[bool] = None
    # Defines the supported Marital Status Type values.
    marital_status: Optional[LeadProfile_maritalStatus] = None
    
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
        from .lead_profile_employment_type import LeadProfile_employmentType
        from .lead_profile_gender import LeadProfile_gender
        from .lead_profile_marital_status import LeadProfile_maritalStatus

        from .lead_profile_employment_type import LeadProfile_employmentType
        from .lead_profile_gender import LeadProfile_gender
        from .lead_profile_marital_status import LeadProfile_maritalStatus

        fields: dict[str, Callable[[Any], None]] = {
            "birthDate": lambda n : setattr(self, 'birth_date', n.get_date_value()),
            "employmentType": lambda n : setattr(self, 'employment_type', n.get_enum_value(LeadProfile_employmentType)),
            "gender": lambda n : setattr(self, 'gender', n.get_enum_value(LeadProfile_gender)),
            "hasBankruptcy": lambda n : setattr(self, 'has_bankruptcy', n.get_bool_value()),
            "hasMedicalCondition": lambda n : setattr(self, 'has_medical_condition', n.get_bool_value()),
            "isHomeowner": lambda n : setattr(self, 'is_homeowner', n.get_bool_value()),
            "maritalStatus": lambda n : setattr(self, 'marital_status', n.get_enum_value(LeadProfile_maritalStatus)),
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
        writer.write_enum_value("employmentType", self.employment_type)
        writer.write_enum_value("gender", self.gender)
        writer.write_bool_value("hasBankruptcy", self.has_bankruptcy)
        writer.write_bool_value("hasMedicalCondition", self.has_medical_condition)
        writer.write_bool_value("isHomeowner", self.is_homeowner)
        writer.write_enum_value("maritalStatus", self.marital_status)
        writer.write_additional_data_value(self.additional_data)
    

