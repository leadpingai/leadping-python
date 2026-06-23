from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .usage_counter_line import UsageCounterLine
    from .usage_summary_line import UsageSummaryLine

@dataclass
class UsageSummaryResponse(AdditionalDataHolder, Parsable):
    """
    API DTO containing usage summary response data.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billable quantity total for this usage summary.
    billable_quantity_total: Optional[float] = None
    # The billing blocked count for this usage summary.
    billing_blocked_count: Optional[int] = None
    # The named usage counters included with this usage summary.
    counters: Optional[list[UsageCounterLine]] = None
    # The customer charge total for this usage summary.
    customer_charge_total: Optional[float] = None
    # The failed count for this usage summary.
    failed_count: Optional[int] = None
    # The internal cost total for this usage summary.
    internal_cost_total: Optional[float] = None
    # The lines included with this usage summary.
    lines: Optional[list[UsageSummaryLine]] = None
    # The non billable internal count for this usage summary.
    non_billable_internal_count: Optional[int] = None
    # The pending invoice count for this usage summary.
    pending_invoice_count: Optional[int] = None
    # The date and time for the period end value on this usage summary.
    period_end: Optional[datetime.datetime] = None
    # The date and time for the period start value on this usage summary.
    period_start: Optional[datetime.datetime] = None
    # The provider cost total for this usage summary.
    provider_cost_total: Optional[float] = None
    # The usage record count for this usage summary.
    usage_record_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageSummaryResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageSummaryResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageSummaryResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .usage_counter_line import UsageCounterLine
        from .usage_summary_line import UsageSummaryLine

        from .usage_counter_line import UsageCounterLine
        from .usage_summary_line import UsageSummaryLine

        fields: dict[str, Callable[[Any], None]] = {
            "billableQuantityTotal": lambda n : setattr(self, 'billable_quantity_total', n.get_float_value()),
            "billingBlockedCount": lambda n : setattr(self, 'billing_blocked_count', n.get_int_value()),
            "counters": lambda n : setattr(self, 'counters', n.get_collection_of_object_values(UsageCounterLine)),
            "customerChargeTotal": lambda n : setattr(self, 'customer_charge_total', n.get_float_value()),
            "failedCount": lambda n : setattr(self, 'failed_count', n.get_int_value()),
            "internalCostTotal": lambda n : setattr(self, 'internal_cost_total', n.get_float_value()),
            "lines": lambda n : setattr(self, 'lines', n.get_collection_of_object_values(UsageSummaryLine)),
            "nonBillableInternalCount": lambda n : setattr(self, 'non_billable_internal_count', n.get_int_value()),
            "pendingInvoiceCount": lambda n : setattr(self, 'pending_invoice_count', n.get_int_value()),
            "periodEnd": lambda n : setattr(self, 'period_end', n.get_datetime_value()),
            "periodStart": lambda n : setattr(self, 'period_start', n.get_datetime_value()),
            "providerCostTotal": lambda n : setattr(self, 'provider_cost_total', n.get_float_value()),
            "usageRecordCount": lambda n : setattr(self, 'usage_record_count', n.get_int_value()),
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
        writer.write_float_value("billableQuantityTotal", self.billable_quantity_total)
        writer.write_int_value("billingBlockedCount", self.billing_blocked_count)
        writer.write_collection_of_object_values("counters", self.counters)
        writer.write_float_value("customerChargeTotal", self.customer_charge_total)
        writer.write_int_value("failedCount", self.failed_count)
        writer.write_float_value("internalCostTotal", self.internal_cost_total)
        writer.write_collection_of_object_values("lines", self.lines)
        writer.write_int_value("nonBillableInternalCount", self.non_billable_internal_count)
        writer.write_int_value("pendingInvoiceCount", self.pending_invoice_count)
        writer.write_datetime_value("periodEnd", self.period_end)
        writer.write_datetime_value("periodStart", self.period_start)
        writer.write_float_value("providerCostTotal", self.provider_cost_total)
        writer.write_int_value("usageRecordCount", self.usage_record_count)
        writer.write_additional_data_value(self.additional_data)
    

