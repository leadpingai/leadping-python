from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_comparison import AnalyticsComparison

@dataclass
class CustomerAnalyticsSummary(AdditionalDataHolder, Parsable):
    """
    Summarizes an organization's primary lead, response, communication, and conversion KPIs for the selected period.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Average time, in minutes, before a lead receives a response.
    average_response_minutes: Optional[float] = None
    # Current billing status for this Leadping customer analytics summary.
    billing_status: Optional[str] = None
    # Total connected call duration, in minutes, during the reporting period.
    call_minutes: Optional[float] = None
    # Number of outbound calls placed during the reporting period.
    calls_placed: Optional[int] = None
    # Number of inbound calls received during the reporting period.
    calls_received: Optional[int] = None
    # Manual provider-accepted SMS messages; automated messages are excluded.
    human_responses: Optional[int] = None
    # Number of leads represented by this Leadping customer analytics summary.
    leads: Optional[int] = None
    # Compares a metric with the preceding period and reports its absolute and percentage change.
    leads_comparison: Optional[AnalyticsComparison] = None
    # Median response minutes measured in minutes.
    median_response_minutes: Optional[float] = None
    # Number of calls missed during the reporting period.
    missed_calls: Optional[int] = None
    # Number of missed leads represented by this Leadping customer analytics summary.
    missed_leads: Optional[int] = None
    # Responses observed through this instant; min(report end plus five minutes, generation time).
    observed_through: Optional[datetime.datetime] = None
    # Timely human responses divided by all mature eligible leads, including unanswered leads.
    overall_five_minute_sla_percent: Optional[float] = None
    # Received prospect messages excluding consent and help commands.
    prospect_replies: Optional[int] = None
    # Conditional percentage: human responses within five minutes divided by responded leads only; not overall coverage.
    responded_within_five_minutes_percent: Optional[float] = None
    # Non-deleted leads created in the cohort with a full five-minute observation window.
    sla_eligible_leads: Optional[int] = None
    # Cohort leads younger than five minutes at ObservedThrough; excluded from SLA denominator.
    sla_pending_leads: Optional[int] = None
    # Mature eligible leads with a human response within exactly five minutes.
    sla_timely_leads: Optional[int] = None
    # Mature eligible leads without a human response by ObservedThrough.
    sla_unresponded_leads: Optional[int] = None
    # Messages whose send execution started; queued and scheduled messages are excluded.
    sms_attempted: Optional[int] = None
    # Messages confirmed delivered, counted at delivery time.
    sms_delivered: Optional[int] = None
    # Number of SMS messages received during the reporting period.
    sms_received: Optional[int] = None
    # Provider-accepted outbound messages, counted at acceptance time (SmsSent is the compatibility field name).
    sms_sent: Optional[int] = None
    # Number of unread messages represented by this Leadping customer analytics summary.
    unread_messages: Optional[int] = None
    # Usage spend represented by this Leadping customer analytics summary.
    usage_spend: Optional[float] = None
    # Wallet balance represented by this Leadping customer analytics summary.
    wallet_balance: Optional[float] = None
    # Current wallet status for this Leadping customer analytics summary.
    wallet_status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerAnalyticsSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerAnalyticsSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerAnalyticsSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_comparison import AnalyticsComparison

        from .analytics_comparison import AnalyticsComparison

        fields: dict[str, Callable[[Any], None]] = {
            "averageResponseMinutes": lambda n : setattr(self, 'average_response_minutes', n.get_float_value()),
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_str_value()),
            "callMinutes": lambda n : setattr(self, 'call_minutes', n.get_float_value()),
            "callsPlaced": lambda n : setattr(self, 'calls_placed', n.get_int_value()),
            "callsReceived": lambda n : setattr(self, 'calls_received', n.get_int_value()),
            "humanResponses": lambda n : setattr(self, 'human_responses', n.get_int_value()),
            "leads": lambda n : setattr(self, 'leads', n.get_int_value()),
            "leadsComparison": lambda n : setattr(self, 'leads_comparison', n.get_object_value(AnalyticsComparison)),
            "medianResponseMinutes": lambda n : setattr(self, 'median_response_minutes', n.get_float_value()),
            "missedCalls": lambda n : setattr(self, 'missed_calls', n.get_int_value()),
            "missedLeads": lambda n : setattr(self, 'missed_leads', n.get_int_value()),
            "observedThrough": lambda n : setattr(self, 'observed_through', n.get_datetime_value()),
            "overallFiveMinuteSlaPercent": lambda n : setattr(self, 'overall_five_minute_sla_percent', n.get_float_value()),
            "prospectReplies": lambda n : setattr(self, 'prospect_replies', n.get_int_value()),
            "respondedWithinFiveMinutesPercent": lambda n : setattr(self, 'responded_within_five_minutes_percent', n.get_float_value()),
            "slaEligibleLeads": lambda n : setattr(self, 'sla_eligible_leads', n.get_int_value()),
            "slaPendingLeads": lambda n : setattr(self, 'sla_pending_leads', n.get_int_value()),
            "slaTimelyLeads": lambda n : setattr(self, 'sla_timely_leads', n.get_int_value()),
            "slaUnrespondedLeads": lambda n : setattr(self, 'sla_unresponded_leads', n.get_int_value()),
            "smsAttempted": lambda n : setattr(self, 'sms_attempted', n.get_int_value()),
            "smsDelivered": lambda n : setattr(self, 'sms_delivered', n.get_int_value()),
            "smsReceived": lambda n : setattr(self, 'sms_received', n.get_int_value()),
            "smsSent": lambda n : setattr(self, 'sms_sent', n.get_int_value()),
            "unreadMessages": lambda n : setattr(self, 'unread_messages', n.get_int_value()),
            "usageSpend": lambda n : setattr(self, 'usage_spend', n.get_float_value()),
            "walletBalance": lambda n : setattr(self, 'wallet_balance', n.get_float_value()),
            "walletStatus": lambda n : setattr(self, 'wallet_status', n.get_str_value()),
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
        writer.write_float_value("averageResponseMinutes", self.average_response_minutes)
        writer.write_str_value("billingStatus", self.billing_status)
        writer.write_float_value("callMinutes", self.call_minutes)
        writer.write_int_value("callsPlaced", self.calls_placed)
        writer.write_int_value("callsReceived", self.calls_received)
        writer.write_int_value("humanResponses", self.human_responses)
        writer.write_int_value("leads", self.leads)
        writer.write_object_value("leadsComparison", self.leads_comparison)
        writer.write_float_value("medianResponseMinutes", self.median_response_minutes)
        writer.write_int_value("missedCalls", self.missed_calls)
        writer.write_int_value("missedLeads", self.missed_leads)
        writer.write_datetime_value("observedThrough", self.observed_through)
        writer.write_float_value("overallFiveMinuteSlaPercent", self.overall_five_minute_sla_percent)
        writer.write_int_value("prospectReplies", self.prospect_replies)
        writer.write_float_value("respondedWithinFiveMinutesPercent", self.responded_within_five_minutes_percent)
        writer.write_int_value("slaEligibleLeads", self.sla_eligible_leads)
        writer.write_int_value("slaPendingLeads", self.sla_pending_leads)
        writer.write_int_value("slaTimelyLeads", self.sla_timely_leads)
        writer.write_int_value("slaUnrespondedLeads", self.sla_unresponded_leads)
        writer.write_int_value("smsAttempted", self.sms_attempted)
        writer.write_int_value("smsDelivered", self.sms_delivered)
        writer.write_int_value("smsReceived", self.sms_received)
        writer.write_int_value("smsSent", self.sms_sent)
        writer.write_int_value("unreadMessages", self.unread_messages)
        writer.write_float_value("usageSpend", self.usage_spend)
        writer.write_float_value("walletBalance", self.wallet_balance)
        writer.write_str_value("walletStatus", self.wallet_status)
        writer.write_additional_data_value(self.additional_data)
    

