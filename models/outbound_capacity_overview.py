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

    # Collection of phone numbers included with this Leadping outbound capacity overview.
    phone_numbers: Optional[list[OutboundPhoneNumberCapacity]] = None
    # Collection of recent decisions included with this Leadping outbound capacity overview.
    recent_decisions: Optional[list[OutboundQueueItem]] = None
    
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
            "phoneNumbers": lambda n : setattr(self, 'phone_numbers', n.get_collection_of_object_values(OutboundPhoneNumberCapacity)),
            "recentDecisions": lambda n : setattr(self, 'recent_decisions', n.get_collection_of_object_values(OutboundQueueItem)),
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
        writer.write_collection_of_object_values("phoneNumbers", self.phone_numbers)
        writer.write_collection_of_object_values("recentDecisions", self.recent_decisions)
        writer.write_additional_data_value(self.additional_data)
    

