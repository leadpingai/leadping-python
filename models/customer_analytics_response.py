from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_date_range import AnalyticsDateRange
    from .customer_activation_health import CustomerActivationHealth
    from .customer_analytics_summary import CustomerAnalyticsSummary
    from .customer_automation_health import CustomerAutomationHealth
    from .customer_communication_usage import CustomerCommunicationUsage
    from .customer_lead_source_breakdown import CustomerLeadSourceBreakdown
    from .customer_lead_trend import CustomerLeadTrend
    from .customer_needs_attention_item import CustomerNeedsAttentionItem
    from .customer_response_metrics import CustomerResponseMetrics

@dataclass
class CustomerAnalyticsResponse(AdditionalDataHolder, Parsable):
    """
    Response model containing customer analytics data returned by the Leadping API.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Activation health associated with this Leadping customer analytics.
    activation_health: Optional[CustomerActivationHealth] = None
    # Automation health associated with this Leadping customer analytics.
    automation_health: Optional[CustomerAutomationHealth] = None
    # Communication usage associated with this Leadping customer analytics.
    communication_usage: Optional[CustomerCommunicationUsage] = None
    # Date and time when this Leadping customer analytics was generated.
    generated_at: Optional[datetime.datetime] = None
    # Collection of lead sources included with this Leadping customer analytics.
    lead_sources: Optional[list[CustomerLeadSourceBreakdown]] = None
    # Lead trend associated with this Leadping customer analytics.
    lead_trend: Optional[CustomerLeadTrend] = None
    # Date and time when this Leadping customer analytics was needs attention.
    needs_attention: Optional[list[CustomerNeedsAttentionItem]] = None
    # Range associated with this Leadping customer analytics.
    range: Optional[AnalyticsDateRange] = None
    # Response metrics associated with this Leadping customer analytics.
    response_metrics: Optional[CustomerResponseMetrics] = None
    # Human-readable summary for this Leadping customer analytics.
    summary: Optional[CustomerAnalyticsSummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerAnalyticsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerAnalyticsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerAnalyticsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .analytics_date_range import AnalyticsDateRange
        from .customer_activation_health import CustomerActivationHealth
        from .customer_analytics_summary import CustomerAnalyticsSummary
        from .customer_automation_health import CustomerAutomationHealth
        from .customer_communication_usage import CustomerCommunicationUsage
        from .customer_lead_source_breakdown import CustomerLeadSourceBreakdown
        from .customer_lead_trend import CustomerLeadTrend
        from .customer_needs_attention_item import CustomerNeedsAttentionItem
        from .customer_response_metrics import CustomerResponseMetrics

        from .analytics_date_range import AnalyticsDateRange
        from .customer_activation_health import CustomerActivationHealth
        from .customer_analytics_summary import CustomerAnalyticsSummary
        from .customer_automation_health import CustomerAutomationHealth
        from .customer_communication_usage import CustomerCommunicationUsage
        from .customer_lead_source_breakdown import CustomerLeadSourceBreakdown
        from .customer_lead_trend import CustomerLeadTrend
        from .customer_needs_attention_item import CustomerNeedsAttentionItem
        from .customer_response_metrics import CustomerResponseMetrics

        fields: dict[str, Callable[[Any], None]] = {
            "activationHealth": lambda n : setattr(self, 'activation_health', n.get_object_value(CustomerActivationHealth)),
            "automationHealth": lambda n : setattr(self, 'automation_health', n.get_object_value(CustomerAutomationHealth)),
            "communicationUsage": lambda n : setattr(self, 'communication_usage', n.get_object_value(CustomerCommunicationUsage)),
            "generatedAt": lambda n : setattr(self, 'generated_at', n.get_datetime_value()),
            "leadSources": lambda n : setattr(self, 'lead_sources', n.get_collection_of_object_values(CustomerLeadSourceBreakdown)),
            "leadTrend": lambda n : setattr(self, 'lead_trend', n.get_object_value(CustomerLeadTrend)),
            "needsAttention": lambda n : setattr(self, 'needs_attention', n.get_collection_of_object_values(CustomerNeedsAttentionItem)),
            "range": lambda n : setattr(self, 'range', n.get_object_value(AnalyticsDateRange)),
            "responseMetrics": lambda n : setattr(self, 'response_metrics', n.get_object_value(CustomerResponseMetrics)),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(CustomerAnalyticsSummary)),
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
        writer.write_object_value("activationHealth", self.activation_health)
        writer.write_object_value("automationHealth", self.automation_health)
        writer.write_object_value("communicationUsage", self.communication_usage)
        writer.write_datetime_value("generatedAt", self.generated_at)
        writer.write_collection_of_object_values("leadSources", self.lead_sources)
        writer.write_object_value("leadTrend", self.lead_trend)
        writer.write_collection_of_object_values("needsAttention", self.needs_attention)
        writer.write_object_value("range", self.range)
        writer.write_object_value("responseMetrics", self.response_metrics)
        writer.write_object_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    

