from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .outbound_phone_number_capacity import OutboundPhoneNumberCapacity
    from .outbound_queue_item import OutboundQueueItem

@dataclass
class OutboundCapacityOverview(AdditionalDataHolder, Parsable):
    """
    Represents outbound capacity overview data used by Leadping.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Total number of blocked records represented by this Leadping outbound capacity overview.
    blocked_count: Optional[int] = None
    # Number of cooling phone numbers represented by this Leadping outbound capacity overview.
    cooling_phone_numbers: Optional[int] = None
    # Number of healthy phone numbers represented by this Leadping outbound capacity overview.
    healthy_phone_numbers: Optional[int] = None
    # Number of limited phone numbers represented by this Leadping outbound capacity overview.
    limited_phone_numbers: Optional[int] = None
    # Collection of phone numbers included with this Leadping outbound capacity overview.
    phone_numbers: Optional[list[OutboundPhoneNumberCapacity]] = None
    # Collection of recent decisions included with this Leadping outbound capacity overview.
    recent_decisions: Optional[list[OutboundQueueItem]] = None
    # Total number of scheduled records represented by this Leadping outbound capacity overview.
    scheduled_count: Optional[int] = None
    # SMS capacity remaining today for the applicable messaging or voice capacity window.
    sms_capacity_remaining_today: Optional[int] = None
    # Voice capacity remaining today for the applicable messaging or voice capacity window.
    voice_capacity_remaining_today: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutboundCapacityOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutboundCapacityOverview
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutboundCapacityOverview()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .outbound_phone_number_capacity import OutboundPhoneNumberCapacity
        from .outbound_queue_item import OutboundQueueItem

        from .outbound_phone_number_capacity import OutboundPhoneNumberCapacity
        from .outbound_queue_item import OutboundQueueItem

        fields: dict[str, Callable[[Any], None]] = {
            "blockedCount": lambda n : setattr(self, 'blocked_count', n.get_int_value()),
            "coolingPhoneNumbers": lambda n : setattr(self, 'cooling_phone_numbers', n.get_int_value()),
            "healthyPhoneNumbers": lambda n : setattr(self, 'healthy_phone_numbers', n.get_int_value()),
            "limitedPhoneNumbers": lambda n : setattr(self, 'limited_phone_numbers', n.get_int_value()),
            "phoneNumbers": lambda n : setattr(self, 'phone_numbers', n.get_collection_of_object_values(OutboundPhoneNumberCapacity)),
            "recentDecisions": lambda n : setattr(self, 'recent_decisions', n.get_collection_of_object_values(OutboundQueueItem)),
            "scheduledCount": lambda n : setattr(self, 'scheduled_count', n.get_int_value()),
            "smsCapacityRemainingToday": lambda n : setattr(self, 'sms_capacity_remaining_today', n.get_int_value()),
            "voiceCapacityRemainingToday": lambda n : setattr(self, 'voice_capacity_remaining_today', n.get_int_value()),
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
        writer.write_int_value("blockedCount", self.blocked_count)
        writer.write_int_value("coolingPhoneNumbers", self.cooling_phone_numbers)
        writer.write_int_value("healthyPhoneNumbers", self.healthy_phone_numbers)
        writer.write_int_value("limitedPhoneNumbers", self.limited_phone_numbers)
        writer.write_collection_of_object_values("phoneNumbers", self.phone_numbers)
        writer.write_collection_of_object_values("recentDecisions", self.recent_decisions)
        writer.write_int_value("scheduledCount", self.scheduled_count)
        writer.write_int_value("smsCapacityRemainingToday", self.sms_capacity_remaining_today)
        writer.write_int_value("voiceCapacityRemainingToday", self.voice_capacity_remaining_today)
        writer.write_additional_data_value(self.additional_data)
    

