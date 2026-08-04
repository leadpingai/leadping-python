from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .current_lead_status_summary_category import CurrentLeadStatusSummary_category
    from .current_lead_status_summary_source import CurrentLeadStatusSummary_source

@dataclass
class CurrentLeadStatusSummary(AdditionalDataHolder, Parsable):
    """
    Summary schema for Leadping API current lead status change summary data used in dashboards and reports.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Controlled lead status change categories used for reporting, automation, and analytics.
    category: Optional[CurrentLeadStatusSummary_category] = None
    # UTC timestamp when the lead status change last changed.
    changed_at: Optional[datetime.datetime] = None
    # Automation ID that last changed the lead status change.
    changed_by_automation_id: Optional[str] = None
    # User ID of the person who last changed the lead status change.
    changed_by_user_id: Optional[str] = None
    # Human-readable display name shown for this current lead status change summary.
    display_name: Optional[str] = None
    # Unique Leadping identifier for this current lead status change summary.
    id: Optional[str] = None
    # Current lead status change outcome assigned to the lead.
    outcome: Optional[str] = None
    # Known sources that can change a lead's current lead status change.
    source: Optional[CurrentLeadStatusSummary_source] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CurrentLeadStatusSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CurrentLeadStatusSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CurrentLeadStatusSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .current_lead_status_summary_category import CurrentLeadStatusSummary_category
        from .current_lead_status_summary_source import CurrentLeadStatusSummary_source

        from .current_lead_status_summary_category import CurrentLeadStatusSummary_category
        from .current_lead_status_summary_source import CurrentLeadStatusSummary_source

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(CurrentLeadStatusSummary_category)),
            "changedAt": lambda n : setattr(self, 'changed_at', n.get_datetime_value()),
            "changedByAutomationId": lambda n : setattr(self, 'changed_by_automation_id', n.get_str_value()),
            "changedByUserId": lambda n : setattr(self, 'changed_by_user_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "outcome": lambda n : setattr(self, 'outcome', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(CurrentLeadStatusSummary_source)),
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
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("changedAt", self.changed_at)
        writer.write_str_value("changedByAutomationId", self.changed_by_automation_id)
        writer.write_str_value("changedByUserId", self.changed_by_user_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("outcome", self.outcome)
        writer.write_enum_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

