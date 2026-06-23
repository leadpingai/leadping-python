from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .outbound_delivery_channel import OutboundDeliveryChannel
    from .outbound_delivery_source import OutboundDeliverySource
    from .outbound_delivery_status import OutboundDeliveryStatus
    from .outbound_queue_item_reason_code import OutboundQueueItem_reasonCode

@dataclass
class OutboundQueueItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines outbound delivery channels protected by delivery control.
    channel: Optional[OutboundDeliveryChannel] = None
    # The id property
    id: Optional[str] = None
    # The phoneNumber property
    phone_number: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # Structured reason codes for outbound pacing and blocking decisions.
    reason_code: Optional[OutboundQueueItem_reasonCode] = None
    # The scheduledSendAt property
    scheduled_send_at: Optional[datetime.datetime] = None
    # Defines the source that requested outbound delivery.
    source: Optional[OutboundDeliverySource] = None
    # Defines durable outbound delivery request statuses.
    status: Optional[OutboundDeliveryStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutboundQueueItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutboundQueueItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutboundQueueItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .outbound_delivery_channel import OutboundDeliveryChannel
        from .outbound_delivery_source import OutboundDeliverySource
        from .outbound_delivery_status import OutboundDeliveryStatus
        from .outbound_queue_item_reason_code import OutboundQueueItem_reasonCode

        from .outbound_delivery_channel import OutboundDeliveryChannel
        from .outbound_delivery_source import OutboundDeliverySource
        from .outbound_delivery_status import OutboundDeliveryStatus
        from .outbound_queue_item_reason_code import OutboundQueueItem_reasonCode

        fields: dict[str, Callable[[Any], None]] = {
            "channel": lambda n : setattr(self, 'channel', n.get_enum_value(OutboundDeliveryChannel)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "reasonCode": lambda n : setattr(self, 'reason_code', n.get_enum_value(OutboundQueueItem_reasonCode)),
            "scheduledSendAt": lambda n : setattr(self, 'scheduled_send_at', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_enum_value(OutboundDeliverySource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OutboundDeliveryStatus)),
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
        writer.write_enum_value("channel", self.channel)
        writer.write_str_value("id", self.id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("reason", self.reason)
        writer.write_enum_value("reasonCode", self.reason_code)
        writer.write_datetime_value("scheduledSendAt", self.scheduled_send_at)
        writer.write_enum_value("source", self.source)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

