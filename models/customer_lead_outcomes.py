from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerLeadOutcomes(AdditionalDataHolder, Parsable):
    """
    Current outcomes for non-deleted, non-demo leads created in the selected period.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Distinct leads with a prospect reply or answered call since creation, through generation time.
    contacted_leads: Optional[int] = None
    # Leads whose current status category is Converted.
    converted_leads: Optional[int] = None
    # Median time to the first manual SMS send attempt or placed outbound call, among attempted leads only.
    median_first_attempt_minutes: Optional[float] = None
    # Enabled, unarchived open or qualified leads with an overdue incomplete follow-up, or neither a manual attempt nor contact.
    needs_follow_up_leads: Optional[int] = None
    # Number of non-deleted, non-demo leads created in the selected period.
    total_leads: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerLeadOutcomes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerLeadOutcomes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerLeadOutcomes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "contactedLeads": lambda n : setattr(self, 'contacted_leads', n.get_int_value()),
            "convertedLeads": lambda n : setattr(self, 'converted_leads', n.get_int_value()),
            "medianFirstAttemptMinutes": lambda n : setattr(self, 'median_first_attempt_minutes', n.get_float_value()),
            "needsFollowUpLeads": lambda n : setattr(self, 'needs_follow_up_leads', n.get_int_value()),
            "totalLeads": lambda n : setattr(self, 'total_leads', n.get_int_value()),
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
        writer.write_int_value("contactedLeads", self.contacted_leads)
        writer.write_int_value("convertedLeads", self.converted_leads)
        writer.write_float_value("medianFirstAttemptMinutes", self.median_first_attempt_minutes)
        writer.write_int_value("needsFollowUpLeads", self.needs_follow_up_leads)
        writer.write_int_value("totalLeads", self.total_leads)
        writer.write_additional_data_value(self.additional_data)
    

