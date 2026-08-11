from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics_comparison import AnalyticsComparison

@dataclass
class CustomerAnalyticsSummary(AdditionalDataHolder, Parsable):
    """
    Represents customer analytics summary data exposed by Leadping analytics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Current billing status for this Leadping customer analytics summary.
    billing_status: Optional[str] = None
    # Date and time when this Leadping customer analytics summary was leads comparison.
    leads_comparison: Optional[AnalyticsComparison] = None
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
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_str_value()),
            "leadsComparison": lambda n : setattr(self, 'leads_comparison', n.get_object_value(AnalyticsComparison)),
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
        writer.write_str_value("billingStatus", self.billing_status)
        writer.write_object_value("leadsComparison", self.leads_comparison)
        writer.write_str_value("walletStatus", self.wallet_status)
        writer.write_additional_data_value(self.additional_data)
    

