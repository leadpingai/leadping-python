from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billable_unit import BillableUnit
    from .usage_channel import UsageChannel
    from .usage_status import UsageStatus

@dataclass
class UsageSummaryLine(AdditionalDataHolder, Parsable):
    """
    Describes usage summary line data used in Leadping API requests and responses.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Billable unit for this usage summary line.
    billable_unit: Optional[BillableUnit] = None
    # Channel for this usage summary line.
    channel: Optional[UsageChannel] = None
    # The current status for this usage summary line.
    status: Optional[UsageStatus] = None
    
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
        from .usage_status import UsageStatus

        from .billable_unit import BillableUnit
        from .usage_channel import UsageChannel
        from .usage_status import UsageStatus

        fields: dict[str, Callable[[Any], None]] = {
            "billableUnit": lambda n : setattr(self, 'billable_unit', n.get_enum_value(BillableUnit)),
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(UsageChannel)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(UsageStatus)),
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
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

