from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerResponseSlaPoint(AdditionalDataHolder, Parsable):
    """
    Five-minute human-response SLA for a lead creation cohort.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Timely leads divided by all eligible leads.
    coverage_percent: Optional[float] = None
    # Mature leads in this bucket.
    eligible_leads: Optional[int] = None
    # End of cohort bucket.
    end_at: Optional[datetime.datetime] = None
    # Bucket label.
    label: Optional[str] = None
    # Leads still within their first five minutes.
    pending_leads: Optional[int] = None
    # Inclusive cohort bucket start.
    start_at: Optional[datetime.datetime] = None
    # Eligible leads answered in five minutes.
    timely_leads: Optional[int] = None
    # Eligible leads unanswered by observation cutoff.
    unresponded_leads: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerResponseSlaPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerResponseSlaPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerResponseSlaPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "coveragePercent": lambda n : setattr(self, 'coverage_percent', n.get_float_value()),
            "eligibleLeads": lambda n : setattr(self, 'eligible_leads', n.get_int_value()),
            "endAt": lambda n : setattr(self, 'end_at', n.get_datetime_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "pendingLeads": lambda n : setattr(self, 'pending_leads', n.get_int_value()),
            "startAt": lambda n : setattr(self, 'start_at', n.get_datetime_value()),
            "timelyLeads": lambda n : setattr(self, 'timely_leads', n.get_int_value()),
            "unrespondedLeads": lambda n : setattr(self, 'unresponded_leads', n.get_int_value()),
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
        writer.write_float_value("coveragePercent", self.coverage_percent)
        writer.write_int_value("eligibleLeads", self.eligible_leads)
        writer.write_datetime_value("endAt", self.end_at)
        writer.write_str_value("label", self.label)
        writer.write_int_value("pendingLeads", self.pending_leads)
        writer.write_datetime_value("startAt", self.start_at)
        writer.write_int_value("timelyLeads", self.timely_leads)
        writer.write_int_value("unrespondedLeads", self.unresponded_leads)
        writer.write_additional_data_value(self.additional_data)
    

