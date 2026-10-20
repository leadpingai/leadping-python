from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .lead_inquiry_urgency import LeadInquiry_urgency

@dataclass
class LeadInquiry(AdditionalDataHolder, Parsable):
    """
    The service or purchase requested by a lead.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Maximum budget in the specified currency.
    budget_maximum: Optional[float] = None
    # Minimum budget in the specified currency.
    budget_minimum: Optional[float] = None
    # ISO 4217 currency code for the budget.
    currency: Optional[str] = None
    # Description of the requested work or purchase.
    description: Optional[str] = None
    # Requested start date.
    desired_start_date: Optional[datetime.date] = None
    # Requested service or product.
    service: Optional[str] = None
    # Supported LeadUrgency values.
    urgency: Optional[LeadInquiry_urgency] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadInquiry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadInquiry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadInquiry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .lead_inquiry_urgency import LeadInquiry_urgency

        from .lead_inquiry_urgency import LeadInquiry_urgency

        fields: dict[str, Callable[[Any], None]] = {
            "budgetMaximum": lambda n : setattr(self, 'budget_maximum', n.get_float_value()),
            "budgetMinimum": lambda n : setattr(self, 'budget_minimum', n.get_float_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "desiredStartDate": lambda n : setattr(self, 'desired_start_date', n.get_date_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "urgency": lambda n : setattr(self, 'urgency', n.get_enum_value(LeadInquiry_urgency)),
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
        writer.write_float_value("budgetMaximum", self.budget_maximum)
        writer.write_float_value("budgetMinimum", self.budget_minimum)
        writer.write_str_value("currency", self.currency)
        writer.write_str_value("description", self.description)
        writer.write_date_value("desiredStartDate", self.desired_start_date)
        writer.write_str_value("service", self.service)
        writer.write_enum_value("urgency", self.urgency)
        writer.write_additional_data_value(self.additional_data)
    

