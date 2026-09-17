from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_trend_point_ofdecimal import AnalyticsTrendPointOfdecimal
    from .customer_response_sla_point import CustomerResponseSlaPoint

@dataclass
class CustomerResponseMetrics(AdditionalDataHolder, Parsable):
    """
    Measures how quickly and consistently an organization responds to leads across supported communication channels.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Average minutes measured in minutes.
    average_minutes: Optional[float] = None
    # Collection of average minutes trend included with this Leadping customer response metrics.
    average_minutes_trend: Optional[list[AnalyticsTrendPointOfdecimal]] = None
    # Exclusive cohort end.
    cohort_end_at: Optional[datetime.datetime] = None
    # Inclusive cohort start.
    cohort_start_at: Optional[datetime.datetime] = None
    # Median minutes measured in minutes.
    median_minutes: Optional[float] = None
    # Number of calls missed during the reporting period.
    missed_calls: Optional[int] = None
    # Responses observed through this instant; min(report end plus five minutes, generation time).
    observed_through: Optional[datetime.datetime] = None
    # Timely human responses divided by all mature eligible leads, including unanswered leads.
    overall_five_minute_sla_percent: Optional[float] = None
    # Number of responded leads represented by this Leadping customer response metrics.
    responded_leads: Optional[int] = None
    # Conditional percentage: human responses within five minutes divided by responded leads only; not overall coverage.
    responded_within_five_minutes_percent: Optional[float] = None
    # Shared definition used in charts and exports.
    response_definition: Optional[str] = None
    # Non-deleted leads created in the cohort with a full five-minute observation window.
    sla_eligible_leads: Optional[int] = None
    # Cohort leads younger than five minutes at ObservedThrough; excluded from SLA denominator.
    sla_pending_leads: Optional[int] = None
    # Mature eligible leads with a human response within exactly five minutes.
    sla_timely_leads: Optional[int] = None
    # Cohort SLA counts and coverage by lead creation bucket.
    sla_trend: Optional[list[CustomerResponseSlaPoint]] = None
    # Mature eligible leads without a human response by ObservedThrough.
    sla_unresponded_leads: Optional[int] = None
    # Number of unread messages represented by this Leadping customer response metrics.
    unread_messages: Optional[int] = None
    # Number of unresponded leads represented by this Leadping customer response metrics.
    unresponded_leads: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerResponseMetrics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerResponseMetrics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerResponseMetrics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_trend_point_ofdecimal import AnalyticsTrendPointOfdecimal
        from .customer_response_sla_point import CustomerResponseSlaPoint

        from .analytics_trend_point_ofdecimal import AnalyticsTrendPointOfdecimal
        from .customer_response_sla_point import CustomerResponseSlaPoint

        fields: dict[str, Callable[[Any], None]] = {
            "averageMinutes": lambda n : setattr(self, 'average_minutes', n.get_float_value()),
            "averageMinutesTrend": lambda n : setattr(self, 'average_minutes_trend', n.get_collection_of_object_values(AnalyticsTrendPointOfdecimal)),
            "cohortEndAt": lambda n : setattr(self, 'cohort_end_at', n.get_datetime_value()),
            "cohortStartAt": lambda n : setattr(self, 'cohort_start_at', n.get_datetime_value()),
            "medianMinutes": lambda n : setattr(self, 'median_minutes', n.get_float_value()),
            "missedCalls": lambda n : setattr(self, 'missed_calls', n.get_int_value()),
            "observedThrough": lambda n : setattr(self, 'observed_through', n.get_datetime_value()),
            "overallFiveMinuteSlaPercent": lambda n : setattr(self, 'overall_five_minute_sla_percent', n.get_float_value()),
            "respondedLeads": lambda n : setattr(self, 'responded_leads', n.get_int_value()),
            "respondedWithinFiveMinutesPercent": lambda n : setattr(self, 'responded_within_five_minutes_percent', n.get_float_value()),
            "responseDefinition": lambda n : setattr(self, 'response_definition', n.get_str_value()),
            "slaEligibleLeads": lambda n : setattr(self, 'sla_eligible_leads', n.get_int_value()),
            "slaPendingLeads": lambda n : setattr(self, 'sla_pending_leads', n.get_int_value()),
            "slaTimelyLeads": lambda n : setattr(self, 'sla_timely_leads', n.get_int_value()),
            "slaTrend": lambda n : setattr(self, 'sla_trend', n.get_collection_of_object_values(CustomerResponseSlaPoint)),
            "slaUnrespondedLeads": lambda n : setattr(self, 'sla_unresponded_leads', n.get_int_value()),
            "unreadMessages": lambda n : setattr(self, 'unread_messages', n.get_int_value()),
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
        writer.write_float_value("averageMinutes", self.average_minutes)
        writer.write_collection_of_object_values("averageMinutesTrend", self.average_minutes_trend)
        writer.write_datetime_value("cohortEndAt", self.cohort_end_at)
        writer.write_datetime_value("cohortStartAt", self.cohort_start_at)
        writer.write_float_value("medianMinutes", self.median_minutes)
        writer.write_int_value("missedCalls", self.missed_calls)
        writer.write_datetime_value("observedThrough", self.observed_through)
        writer.write_float_value("overallFiveMinuteSlaPercent", self.overall_five_minute_sla_percent)
        writer.write_int_value("respondedLeads", self.responded_leads)
        writer.write_float_value("respondedWithinFiveMinutesPercent", self.responded_within_five_minutes_percent)
        writer.write_str_value("responseDefinition", self.response_definition)
        writer.write_int_value("slaEligibleLeads", self.sla_eligible_leads)
        writer.write_int_value("slaPendingLeads", self.sla_pending_leads)
        writer.write_int_value("slaTimelyLeads", self.sla_timely_leads)
        writer.write_collection_of_object_values("slaTrend", self.sla_trend)
        writer.write_int_value("slaUnrespondedLeads", self.sla_unresponded_leads)
        writer.write_int_value("unreadMessages", self.unread_messages)
        writer.write_int_value("unrespondedLeads", self.unresponded_leads)
        writer.write_additional_data_value(self.additional_data)
    

