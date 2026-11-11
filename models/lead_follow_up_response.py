from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .current_lead_status_summary import CurrentLeadStatusSummary

@dataclass
class LeadFollowUpResponse(AdditionalDataHolder, Parsable):
    """
    Current, visible follow-up work for a lead, independent of stale historical dates.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the lead requiring follow-up.
    lead_id: Optional[str] = None
    # Display name of the lead requiring follow-up.
    lead_name: Optional[str] = None
    # Summary schema for Leadping API current lead status change summary data used in dashboards and reports.
    status: Optional[CurrentLeadStatusSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LeadFollowUpResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LeadFollowUpResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LeadFollowUpResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .current_lead_status_summary import CurrentLeadStatusSummary

        from .current_lead_status_summary import CurrentLeadStatusSummary

        fields: dict[str, Callable[[Any], None]] = {
            "leadId": lambda n : setattr(self, 'lead_id', n.get_str_value()),
            "leadName": lambda n : setattr(self, 'lead_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(CurrentLeadStatusSummary)),
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
        writer.write_str_value("leadId", self.lead_id)
        writer.write_str_value("leadName", self.lead_name)
        writer.write_object_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

