from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billable_unit import BillableUnit
    from .usage_channel import UsageChannel
    from .usage_record_status import UsageRecordStatus

@dataclass
class UsageSummaryLine(AdditionalDataHolder, Parsable):
    """
    API DTO containing usage summary line data used by Leadping API contracts.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billable unit value for this usage summary line.
    billable_unit: Optional[BillableUnit] = None
    # The channel value for this usage summary line.
    channel: Optional[UsageChannel] = None
    # The monetary customer charge amount for this usage summary line.
    customer_charge_amount: Optional[float] = None
    # The quantity value for this usage summary line.
    quantity: Optional[float] = None
    # The record count for this usage summary line.
    record_count: Optional[int] = None
    # The current status for this usage summary line.
    status: Optional[UsageRecordStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageSummaryLine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageSummaryLine
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageSummaryLine()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billable_unit import BillableUnit
        from .usage_channel import UsageChannel
        from .usage_record_status import UsageRecordStatus

        from .billable_unit import BillableUnit
        from .usage_channel import UsageChannel
        from .usage_record_status import UsageRecordStatus

        fields: dict[str, Callable[[Any], None]] = {
            "billableUnit": lambda n : setattr(self, 'billable_unit', n.get_enum_value(BillableUnit)),
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(UsageChannel)),
            "customerChargeAmount": lambda n : setattr(self, 'customer_charge_amount', n.get_float_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_float_value()),
            "recordCount": lambda n : setattr(self, 'record_count', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(UsageRecordStatus)),
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
        writer.write_enum_value("billableUnit", self.billable_unit)
        writer.write_enum_value("channel", self.channel)
        writer.write_float_value("customerChargeAmount", self.customer_charge_amount)
        writer.write_float_value("quantity", self.quantity)
        writer.write_int_value("recordCount", self.record_count)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

