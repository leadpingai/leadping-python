from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_qualification_employment_type import LeadQualification_employmentType
    from .lead_qualification_marital_status import LeadQualification_maritalStatus

@dataclass
class LeadQualification(AdditionalDataHolder, Parsable):
    """
    Optional consumer qualification details for workflows that need them.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Exact credit score supplied by the intake source; not a range.
    credit_score: Optional[int] = None
    # Classifies a lead's reported employment arrangement for qualification and demographic workflows.
    employment_type: Optional[LeadQualification_employmentType] = None
    # Indicates whether the lead reported bankruptcy history.
    has_bankruptcy: Optional[bool] = None
    # Indicates whether the lead reported a medical condition relevant to qualification.
    has_medical_condition: Optional[bool] = None
    # Height in inches.
    height: Optional[int] = None
    # Annual income amount in the specified IncomeCurrency.
    income: Optional[int] = None
    # ISO 4217 currency code for annual income.
    income_currency: Optional[str] = None
    # Indicates whether the lead owns their home.
    is_homeowner: Optional[bool] = None
    # Classifies a lead's reported marital status when required by a qualification or integration workflow.
    marital_status: Optional[LeadQualification_maritalStatus] = None
    # Number of months the lead has lived at the current residence.
    months_at_residence: Optional[int] = None
    # Number of dependents reported by the lead.
    number_of_dependents: Optional[int] = None
    # Body weight in pounds.
    weight: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadQualification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadQualification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadQualification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_qualification_employment_type import LeadQualification_employmentType
        from .lead_qualification_marital_status import LeadQualification_maritalStatus

        from .lead_qualification_employment_type import LeadQualification_employmentType
        from .lead_qualification_marital_status import LeadQualification_maritalStatus

        fields: dict[str, Callable[[Any], None]] = {
            "creditScore": lambda n : setattr(self, 'credit_score', n.get_int_value()),
            "employmentType": lambda n : setattr(self, 'employment_type', n.get_enum_value(LeadQualification_employmentType)),
            "hasBankruptcy": lambda n : setattr(self, 'has_bankruptcy', n.get_bool_value()),
            "hasMedicalCondition": lambda n : setattr(self, 'has_medical_condition', n.get_bool_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "income": lambda n : setattr(self, 'income', n.get_int_value()),
            "incomeCurrency": lambda n : setattr(self, 'income_currency', n.get_str_value()),
            "isHomeowner": lambda n : setattr(self, 'is_homeowner', n.get_bool_value()),
            "maritalStatus": lambda n : setattr(self, 'marital_status', n.get_enum_value(LeadQualification_maritalStatus)),
            "monthsAtResidence": lambda n : setattr(self, 'months_at_residence', n.get_int_value()),
            "numberOfDependents": lambda n : setattr(self, 'number_of_dependents', n.get_int_value()),
            "weight": lambda n : setattr(self, 'weight', n.get_int_value()),
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
        writer.write_int_value("creditScore", self.credit_score)
        writer.write_enum_value("employmentType", self.employment_type)
        writer.write_bool_value("hasBankruptcy", self.has_bankruptcy)
        writer.write_bool_value("hasMedicalCondition", self.has_medical_condition)
        writer.write_int_value("height", self.height)
        writer.write_int_value("income", self.income)
        writer.write_str_value("incomeCurrency", self.income_currency)
        writer.write_bool_value("isHomeowner", self.is_homeowner)
        writer.write_enum_value("maritalStatus", self.marital_status)
        writer.write_int_value("monthsAtResidence", self.months_at_residence)
        writer.write_int_value("numberOfDependents", self.number_of_dependents)
        writer.write_int_value("weight", self.weight)
        writer.write_additional_data_value(self.additional_data)
    

